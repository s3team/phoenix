import re
from definition import *
from register import *

pattern = r"\$(.*?)\$"
rep = re.compile(pattern)


def get_template_str(template_info):
    return template_info[1][0]


def get_template_info(template_info):
    return template_info[1][1]


class FixInfo(object):
    def __init__(self, actions, uses, operand_idx):
        self.actions = actions
        self.use_type = uses
        # if use_type == USE_REG, operand_idx will be register id
        self.operand_idx = operand_idx

    def __str__(self):
        outputs = list()
        output_actions = list()
        output_use = list()
        actions_dict = {ACTION_NEW: "new", ACTION_POP: "pop",
                        ACTION_PUSH: "push", ACTION_EXIST: "exist", ACTION_NONE: "none"}
        use_dict = {USE_OP: "op", USE_REG: "reg", USE_NONE: "none"}

        for action, action_str in actions_dict.items():
            if(self.actions & action):
                output_actions.append(action_str)

        for use, use_str in use_dict.items():
            if(self.use_type == use):
                output_use.append(use_str)

        outputs.append("action:" + "|".join(output_actions))
        outputs.append("use_type:" + "|".join(output_use))
        outputs.append("operand_idx:" + str(self.operand_idx))

        return ", ".join(outputs)


class InstTemplate(object):
    def __init__(self, opcode, operand_list, fix_template, fix_info_list):
        self.opcode = opcode
        self.operand_list = operand_list
        self.fix_template = fix_template

        self.fix_info_list = [FixInfo(i[0], i[1], i[2]) for i in fix_info_list]

    def __str__(self):
        output = ""
        output += "\topcode:\t%s\n" % self.opcode
        output += "\toperand_list:\t%s\n" % str(self.operand_list)
        output += "\tfix_template:\t%s\n" % str(self.fix_template)
        output += "\tfix_info_list:\t%s\n" % str([str(i)
                                                  for i in self.fix_info_list])

        return output


class InstTemplateGenerator(object):
    def __init__(self, templates_info):
        '''
            template_info: string
        '''
        # self.template = dict(inst_signature: template)
        self.templates = self.analyze_templates(templates_info)

    def analyze_templates(self, info):
        '''
            template = {asm_opcode: 
                            [
                                [asm_opcode = mov, operand_list = [op1, op2]], 
                                [c_style_str = "int FIXME = FIXME;", 
                                    [
                                        fix_info = [ACTION_NEW|ACTION_EXIST, USE_OP, index_in_operand_list = 0],
                                        fix_info = [......]
                                    ]
                                ]
                            ]
                        }
        '''
        templates = dict()

        for each_temp in info.split("----"):
            asm_part, c_part = each_temp.strip().split(">>>>")

            # break down asm part
            asm_part = asm_part.strip().split(" ")
            asm_opcode = asm_part[0]

            if(len(asm_part) == 2):
                asm_operands = asm_part[1].strip().split(",")
                asm_operand_list = [i.strip() for i in asm_operands]
            elif(len(asm_part) == 3):
                print("error in asm part breakdown")

            # break down c part
            fix_info_list = list()
            c_part = c_part.strip()
            replace_keyword = rep.findall(c_part)
            for i in replace_keyword:
                keyword_type, replace_target, replace_action = self.analyze_keyword(
                    i)
                replace_loc = None
                if(keyword_type == USE_OP):
                    replace_loc = asm_operand_list.index(replace_target)
                elif(keyword_type == USE_REG):
                    replace_loc = reg_bit_map[replace_target]
                fix_info_list.append(
                    [replace_action, keyword_type, replace_loc])
            fix_template = rep.sub("FIXME", c_part, 0)

            if(len(fix_info_list) == 0):
                fix_info_list.append([ACTION_NONE, USE_NONE, 0])

            templates[opcode_map[asm_opcode]] = InstTemplate(
                asm_opcode, asm_operand_list, fix_template, fix_info_list)

        return templates

    def analyze_keyword(self, keyword):
        replace_action = 0x0
        for action_keyword, action_val in action_map.items():
            if(action_keyword in keyword):
                replace_action = replace_action | action_val
                keyword = keyword.replace(action_keyword, "")
        keyword_type = self.get_keyword_type(keyword)
        return [keyword_type, keyword, replace_action]

    def get_keyword_type(self, keyword):
        if(keyword in reg_bit_map.keys()):
            return USE_REG
        elif(keyword == ""):
            return USE_NONE

        return USE_OP

    def add_a_template(self, template_info):
        pass
