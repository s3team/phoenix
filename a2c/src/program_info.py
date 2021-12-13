import re

from define import *
from register import *
from runtime_info import RuntimeInfo
import queue
from util import *


class Operand(object):

    def __init__(self, op_str: str = None, data_sec: bool = False) -> None:
        self.type: int = 0

        self.is_call_addr: bool = False
        # self.is_deference: bool = False
        self.deference_type: str = MASK_32_BIT

        self.immediate_val: str = None
        self.registers: dict[Register, int] = dict()

        self.label: str = None
        self.is_const_label: bool = False

        # for string reassembly
        self.raw_string: str = op_str

        if op_str:
            rep_offset = re.compile(r"^[*]?(.+?)(?=[(])")
            rep_imm = re.compile(r"[$](.+?)(?=[,)]|$)")
            rep_reg = re.compile(r"[%](.+?)(?=[,)]|$)")
            rep_scale = re.compile(r"[,](\d+?)[)]")
            rep_scale_hex = re.compile(r"[,0x](\d+?)[)]")
            rep_def = re.compile(r"[(](.+?)[)]")

            self.is_call_addr = "*" in op_str

            if "(," in op_str:
                op_str_list = list(op_str)
                op_str_list.insert(op_str.find("(,")+1, "%null")
                op_str = ''.join(op_str_list)

            const_arr = rep_offset.match(op_str)
            if not const_arr:
                const_arr = rep_imm.match(op_str)
            if const_arr:
                const_val = const_arr.group(1)
                if const_val.startswith("0x") or const_val.startswith("-0x"):
                    self.immediate_val = const_val
                    self.type |= OP_IMM
                else:
                    self.label = const_val
                    self.type |= OP_LBL

            reg_arr = rep_reg.findall(op_str)
            try:
                if (reg_arr[0] != "null"):
                    self.registers[reg_name_map[reg_arr[0]]] = 1
            except IndexError:
                pass
            except KeyError:
                assert (reg_arr[0] in reg_name_map) or (reg_arr[0] == "null"), \
                    "no records of %"+reg_arr[0]+" in reg_name_map"
            else:
                self.type |= OP_REG

                scale = rep_scale.search(op_str)
                if not scale:
                    scale = rep_scale_hex.search(op_str)
                try:
                    if scale:
                        self.registers[reg_name_map[reg_arr[1]]
                                       ] = int(scale.group(1))
                    else:
                        self.registers[reg_name_map[reg_arr[1]]] = 1
                except IndexError:
                    pass
                except KeyError:
                    assert reg_arr[1] in reg_name_map, \
                        "no records of %"+reg_arr[1]+" in reg_name_map"

            if self.type & (OP_REG | OP_IMM) == 0:
                self.type |= OP_LBL
                self.label = self.raw_string

            if (rep_def.search(op_str)) or ((self.type & OP_LBL == OP_LBL) and (data_sec)):
                self.type |= OP_DEF

            # self.is_deference = (self.type & OP_DEF == OP_DEF)

            if self.type & OP_LBL:
                if self.label.startswith("$"):
                    self.label = self.label[1:]
                    self.is_const_label = True
                else:
                    label_pos = op_str.find(self.label, 1)
                    if label_pos:
                        self.is_const_label = (op_str[label_pos-1] == "$")

    def set(self, type: int = None, immediate_val: str = None, registers=None, label: str = None, deference_type: str = None) -> None:
        self.type = type
        # self.is_deference = (self.type & OP_DEF == OP_DEF)
        if isinstance(immediate_val, int):
            self.immediate_val = hex(immediate_val)
        else:
            self.immediate_val = immediate_val
        self.registers = registers
        self.label = label
        if deference_type:
            self.deference_type = deference_type

    def get_variables(self, RTInfo: RuntimeInfo = None) -> str:
        add = "+"
        variables = []
        for reg in self.registers:

            assert self.registers[reg], "no records of %" + \
                reg.name+" in operand"
            assert RTInfo.get_var(reg), "no records of %" + \
                reg.name+" in RunTimeInfo"

            reg_str = RTInfo.get_var(reg).join(reg.get_var())
            if self.registers[reg] == 1:
                variables.append(reg_str)
            else:
                variables.append(str(self.registers[reg]) + "*" + reg_str)

        return add.join(variables)

    def get_val(self, RTInfo: RuntimeInfo = None, data_label: bool = False) -> str:
        '''
            get exact value.
            The example here we should:
                1. find rax corresponding variable. i.e., v1
                2. add immediate_val
                3. deference
            result: *(v1+0x400000)
        '''
        val = ""
        if (self.type & OP_REG):
            assert RTInfo, "no RunTime information while mapping register to variable"
            val += self.get_variables(RTInfo)
            if ((self.type & OP_IMM) and (not self.immediate_val.startswith("-0x"))) or (self.type & OP_LBL):
                val += "+"
        if (self.type & OP_IMM):
            val += self.immediate_val
        elif (self.type & OP_LBL):
            val += self.label

        if (self.is_deference()) | (data_label):
            if (self.type & OP_REG) | (self.type & OP_LBL):
                deference_type_dict = {
                    MASK_32_BIT: "int", MASK_16_BIT: "short", MASK_H8_BIT: "char", MASK_L8_BIT: "char"}
                val = "*(unsigned {} *)(".format(
                    deference_type_dict[self.deference_type]) + val + ")"

        return val

    def __str__(self) -> str:
        '''
            Reassemble object Operand to string, for unit test only

            NOTE: Assume no operand like `0xff(%rax,%rbx)` or `0xff(%rax,%rbx,1)`,
            in which case, the reassembly string will mess up two registers.
        '''

        reg_str_list = ["", "", ""]
        for reg in self.registers:
            if self.registers[reg] > 1:
                reg_str_list[1] = "%" + reg.name
                reg_str_list[2] = hex(self.registers[reg])
            else:
                reg_str_list[0] = "%" + reg.name

        reg_str = ""
        if reg_str_list[2]:
            reg_str = ",".join(reg_str_list)
        elif reg_str_list[0]:
            reg_str = reg_str_list[0]

        reassembly = ""
        if self.type & OP_DEF:
            if self.type & OP_IMM:
                reassembly = self.immediate_val + "(" + reg_str + ")"
            elif self.type & OP_LBL:
                if self.is_const_label:
                    reassembly = "$"
                reassembly += self.label + "(" + reg_str + ")"
            else:
                reassembly = "(" + reg_str + ")"
        else:
            if self.type & OP_IMM:
                reassembly = "$" + self.immediate_val
            elif self.type & OP_LBL:
                if self.is_const_label:
                    reassembly = "$"
                reassembly += self.label
            else:
                reassembly = reg_str

        if self.is_call_addr:
            reassembly = "*" + reassembly

        assert reassembly == self.raw_string, "Reassembly Operand String Error: \n\traw: {}\n\treassembly: {}\n{}".format(
            self.raw_string, reassembly, self.registers)

        return reassembly

    def contain_label(self) -> bool:
        return (self.type & OP_LBL == OP_LBL)

    def is_label(self) -> bool:
        return ((self.type | OP_DEF) == (OP_LBL | OP_DEF))

    def is_deference(self) -> bool:
        return (self.type & OP_DEF == OP_DEF)

    def set_data_label(self, flag: bool = True) -> None:
        assert self.is_label(), "Set Data Label for Non-label Operand!"
        self.type |= OP_DEF


class Instruction(object):
    def __init__(self, opcode, operands, basicblock):
        self.operands = list()
        self.basicblock = basicblock

        # if(opcode not in opcode_map.keys()):
        #    opcode_map[opcode] = gen_new_opcode()
        assert opcode in opcode_map.keys(
        ), "Currently unsupported auto add opcode, plz manually add opcode: {}".format(opcode)

        self.opcode = opcode_map[opcode]
        for operand_s in operands:
            self.operands.append(Operand(operand_s))

        # handle auto cast reg -> mem type cast
        mem_type_cast = None
        has_mem_operand = False
        if(self.opcode in auto_cast_opcodes):
            if (len(self.operands) == 2):
                # find src reg operand
                if(self.operands[0].is_deference() == False and len(self.operands[0].registers.keys()) == 1):
                    # fine dst mem operand
                    if(self.operands[1].is_deference()):
                        self.operands[1].deference_type = list(
                            self.operands[0].registers.keys())[0].value_mask

            # Currently, we assume all auto case labels come from data section.
            if self.operands[0].is_label():
                self.operands[0].set_data_label()

    def __str__(self):
        res = ""
        for name, val in opcode_map.items():
            if(val == self.opcode):
                res += name
                break
        res += " " + ",".join([str(i) for i in self.operands])
        return res


class BasicBlock(object):
    def __init__(self, bb_name, inst_list):
        self.name = bb_name
        self.insts = list()
        for inst in inst_list:
            inst_dict = split_inst(inst)
            for opcode, operand_list in inst_dict.items():
                self.insts.append(Instruction(opcode, operand_list, bb_name))

        # todo
        self.successor = list()
        self.preceding = list()

    def __str__(self):
        res = ""
        res += self.name + '\n'
        res += '\n'.join([str(i) for i in self.insts])
        return res


class Function(object):
    def __init__(self, entrance, name):
        self.func_name = name
        self.basicblocks = list()
        self.entrance = entrance


class Program(object):
    def __init__(self, entrance=None):
        self.funcs = list()
        self.entrance = entrance


class GlobalVariable(object):
    def __init__(self, name, values: list, sec_name, is_ptr):
        self.name = name
        self.values = values
        self.sec_name = sec_name
        self.is_ptr = is_ptr

    def __str__(self):
        res = ""
        if self.sec_name == '.rodata':
            res += "const "
        if self.is_ptr: res += "void * "
        else: res += "unsigned char "
        res += self.name
        res += ("[" + str(len(self.values)) + "]")
        res += " = "
        res += "{"
        if self.sec_name == '.bss': res += "0x00"
        else:
            for v in self.values:
                if self.is_ptr: res += ("&" + v + ",")
                else: res += (v + ",")
        res += "};\n"
        return res
