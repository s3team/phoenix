from program_info import *
from runtime_info import *
from inst_template import *
from definition import *
from util import *
from register import *


class Translator(object):
    def __init__(self, templates_info, program, runtime_info):
        self.runtime_info = runtime_info
        self.templates_info = templates_info
        self.program = program
        self.output = list(dict())  # list(dict(func_name:c_code))

    def set_program(self, program):
        pass

    def translate_inst_from_templates(self, inst):
        """
            translate an inst to c code directly, core part of translate_inst
        """
        inst_opcode = inst.opcode
        inst_operands = inst.operands

        inst_template = self.templates_info[inst_opcode]
        fix_template = inst_template.fix_template
        fix_info_list = inst_template.fix_info_list

        for fix_info in fix_info_list:
            real_var = None
            # handle register operation
            if(fix_info.use_type == USE_REG):
                reg_id = fix_info.operand_idx
                real_var = self.runtime_info.reg_var_map.get_var(reg_id)
            # handle operand operation
            elif(fix_info.use_type == USE_OP):
                op_idx = fix_info.operand_idx
                if(fix_info.actions & ACTION_EXIST):
                    real_var = inst_operands[op_idx].get_val(self.runtime_info)
                if(fix_info.actions & ACTION_NEW):
                    # leave it here to see whether we need it
                    pass
            elif(fix_info.use_type == USE_NONE):
                if(fix_info.actions & ACTION_NONE):
                    # no replace
                    real_var = ""
                    pass

            fix_template = fix_template.replace("FIXME", real_var, 1)

        return fix_template

    def translate_inst(self, inst):
        pass

    def translate_bb(self, basicblock):
        pass

    def translate_func(self, function):
        output = str()

        output += "unsigned int {}(){{\n".format(function.func_name)
        for bb in function.basicblocks:
            if(bb != function.basicblocks[0]):
                output += "\t{}:\n".format(bb.name)
            for inst in bb.insts:
                output += "\t\t{}\n".format(
                    self.translate_inst_from_templates(inst))
        output += "}\n"

        return output

    def translate_program(self, program, GVlist: list() = ()):
        output = str()
        func_decls = str()

        for func in program.funcs[::-1]:
            func_decls += "unsigned int {}();\n".format(func.func_name)
            output += self.translate_func(func) + "\n"

        output = func_decls + "\n\n" + output
        for GV in GVlist:
            output = str(GV) + output
        return output
