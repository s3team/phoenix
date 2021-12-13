import re

rep = re.compile(r"[ \t]+")

VAR_ID = 0


def gen_new_var():
    global VAR_ID
    VAR_ID += 1
    return "var" + str(VAR_ID)


def split_inst(inst):
    '''
        input: one line asm instruction string
        output: {opcode: [operands]} in string
    '''
    stack = list()

    inst = rep.sub(" ", inst, 0)
    cur = ""
    skip_space = False
    for i in inst:
        if(i == " " and not skip_space and cur != ""):
            stack.append(cur)
            cur = ""
            skip_space = True

        elif(i == "," and "(" not in cur):
            if(cur != ""):
                stack.append(cur)
                cur = ""

        elif(i == ")" and cur != ""):
            cur += i
            stack.append(cur)
            cur = ""
        else:
            cur += i

    if(cur != ""):
        stack.append(cur)
    return {stack[:1][0]: stack[1:]}


def split_basicblock(program):
    '''
        input: asm program in string
        output: {"label_name":["inst1", "inst2"]}
    '''
    bbs = dict()
    cur_bb = list()
    cur_label = str()

    for line in program.split("\n"):
        if(line == "" or line.startswith(".")):
            continue
        if(line.endswith(":")):
            if(len(cur_bb) > 0):
                bbs[cur_label[:-1]] = cur_bb
                cur_bb = list()
            cur_label = line
        else:
            cur_bb.append(line)

    if(len(cur_bb) > 0):
        bbs[cur_label[:-1]] = cur_bb

    return bbs


def split_section(program):
    '''
        input: asm program in string
        output: {"label_name":str}
    '''
    secs: dict[str, str] = dict()
    current_label: str = str()

    for line in program.split("\n"):
        if(line == ""):
            continue
        if(line.startswith(".section")):
            current_label = line[line.find(".", 7):].split(',')[0]
            secs[current_label] = str()
        elif current_label:
            secs[current_label] += line + "\n"

    return secs


def remove_redundant_code(program, ctors_section):
    def helper(x:str):
        return not (x.startswith('.globl') or x.startswith('endbr'))
    lines = list(filter(helper, program.split('\n')))
    
    useless_bbs = set()
    for line in ctors_section.split('\n'):
        if line.startswith('.long'):
            useless_bbs.add(line.split()[1])
            # queue.append(line.split()[1])
    for i in range(len(lines)):
        if lines[i].startswith('main:'): lines[i+1] = ''
        if re.search(r'add \$_GLOBAL_OFFSET_TABLE_,%[0-9a-z]*', lines[i]):
            useless_bbs.add(lines[i-1].split()[1])
            lines[i-1] = ''
            lines[i] = ''
    bbs = split_basicblock('\n'.join(lines))
    for label, instrs in bbs.items():
        if 'hlt' in instrs: useless_bbs.add(label)
        if 'xchg %ax,%ax' in instrs: useless_bbs.add(label)
        if 'nop;nop;nop;nop;nop;nop;nop;' in instrs: useless_bbs.add(label)
    
    bb_name_list = list(bbs.keys())
    bb_count = len(bb_name_list)
    queue = list(useless_bbs)
    while queue:
        cur_label = queue.pop(0)
        cur_instrs = bbs[cur_label]
        for inst in cur_instrs:
            m = re.search(r'call (S_0x[0-9A-F]*)',inst)
            if m:
                succ_label = m.group(1)
                if succ_label not in bb_name_list: continue
                if succ_label not in useless_bbs:
                    useless_bbs.add(succ_label)
                    queue.append(succ_label)
            m = re.search(r'lea (S_0x[0-9A-F]*),%[0-9a-z]*',inst)
            if m:
                succ_label = m.group(1)
                if succ_label not in bb_name_list: continue
                if succ_label not in useless_bbs:
                    useless_bbs.add(succ_label)
                    queue.append(succ_label)
        if cur_instrs[-1].startswith('j'):
            succ_label = inst.split()[1]
            if succ_label not in useless_bbs:
                useless_bbs.add(succ_label)
                queue.append(succ_label)
        if not (cur_instrs[-1].startswith('jmp') or cur_instrs[-1].startswith('ret') or cur_instrs[-1].startswith('hlt')):
            cur_idx = bb_name_list.index(cur_label)
            if cur_idx + 1 >= bb_count: continue
            succ_label = bb_name_list[cur_idx + 1]
            if succ_label not in useless_bbs:
                useless_bbs.add(succ_label)
                queue.append(succ_label)


    new_program = ''
    for label, instrs in bbs.items():
        if label not in useless_bbs:
            new_program += (label + ':\n' + '\n'.join(instrs) + '\n')
        # else:
        #     print('\n'.join(instrs))
        #     print('\n\n')
    return new_program
