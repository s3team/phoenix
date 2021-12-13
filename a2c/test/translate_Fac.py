tbl_id = 0
def get_new_tbl_id():
    global tbl_id

    tbl_id += 1
    return tbl_id

def translate(inst):
    '''
        translate one asm inst to c code.
    '''
    ccode = str()
    if(inst.endswith(":")):
        ccode = inst
    elif(inst.startswith("push %ebp")):
        ccode = "esp -= 4;\n*(unsigned int*)esp = ebp;"
    elif(inst.startswith("mov %esp,%ebp")):
        ccode = "ebp = esp;"
    elif(inst.startswith("sub $0x10,%esp")):
        ccode = "esp -= 0x10;"
    elif(inst.startswith("movl $0x1,-0x4(%ebp)")):
        ccode = "*(unsigned int *)(ebp-0x4) = 0x1;"
    elif(inst.startswith("jmp B_1")):
        ccode = "goto B_1;"
    elif(inst.startswith("mov -0x4(%ebp),%eax")):
        ccode = "eax = *(unsigned int *)(ebp-0x4);"
    elif(inst.startswith("imul 0x8(%ebp),%eax")):
        ccode = "eax *= *(unsigned int *)(ebp+0x8);"
    elif(inst.startswith("mov %eax,-0x4(%ebp)")):
        ccode = "*(unsigned int *)(ebp-0x4) = eax;"
    elif(inst.startswith("subl $0x1,0x8(%ebp)")):
        ccode = "*(unsigned int *)(ebp+0x8) -= 0x1;"
    elif(inst.startswith("cmpl $0x1,0x8(%ebp)")):
        ccode = "tmp = *(unsigned int *)(ebp+0x8) - 1;"
    elif(inst.startswith("jg B_0")):
        ccode = "if(tmp > 0) goto B_0;"
    elif(inst.startswith("mov -0x4(%ebp),%eax")):
        ccode = "eax = *(unsigned int *)(ebp-0x4);"
    elif(inst.startswith("leave")):
        ccode = "esp = ebp;\nebp = (esp += 4, *((unsigned int*)esp-1));"
    elif(inst.startswith("ret")):
        ccode = "goto RET_ADDR_TBL;"
    elif(inst.startswith("and $0xfffffff0,%esp")):
        ccode = "esp &= 0xfffffff0;"
    elif(inst.startswith("movl $0xa,(%esp)")):
        ccode = "*(unsigned int *)(esp) = 0xa;"
    elif(inst.startswith("call fac")):
        idx = get_new_tbl_id()
        ccode = "esp -= 4;\n*(unsigned int*)esp = %d;\ngoto fac;\nRET_ADDR_%d:" % (idx, idx)
    
    # print("translate: " + inst + "     result:" + ccode)
    return ccode

def read_file(filename):
    with open(filename) as f:
        content = f.read()
    
    while("  " in content):
        content = content.replace("  ", " ")
    return content

def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    
def generate_ret_tbl():
    global tbl_id

    ret_tbl = "RET_ADDR_TBL:\n"
    ret_tbl += "tbl_id = (esp += 4, *((unsigned int*)esp-1));\n"
    ret_tbl += "switch(tbl_id){\n"
    for idx in range(tbl_id):
        ret_tbl += "case %d:\n\tgoto RET_ADDR_%d;\n" % (idx+1, idx+1)
    ret_tbl += "}"

    return ret_tbl

def generate_reg_var():
    output = str()
    reg_list = ["eax", "ebx", "ecx", "edx", "edi", "ebp", "esi", "esp"]

    for reg in reg_list:
        output += "unsigned int %s = 0;\n" % (reg)

    return output

def generate_stack():
    return "\nunsigned char * stack;\nstack = (char*)malloc(6291456);\nesp = ebp = (int)stack + 6291456 - 4;\nint tmp, tbl_id;\n"

def main(asm_file_path):
    ccodes = str()
    for inst in read_file(asm_file_path).split("\n"):
        # print inst
        ccodes += translate(inst) + "\n"
    
    ccodes = generate_stack() + "\ngoto main;\n" + ccodes
    ccodes = ccodes + "\nreturn 0;\n" + generate_ret_tbl()
    ccodes = ccodes.replace("main", "usermain")
    ccodes = ccodes.replace("\n", "\n\t")
    
    output = "#include <stdio.h>\n#include <stdlib.h>\n\n\n\n" + generate_reg_var() + "int main(){\n" + ccodes + "\n}\n"
    return output

if(__name__ == "__main__"):
    write_file("Fac.c", main("../benchmark/Fac.s"))