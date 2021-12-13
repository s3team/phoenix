import os
import re

from test_util import *
import util
from define import *
from program_info import Operand
from runtime_info import RuntimeInfo


static_RTI = RuntimeInfo(arch=ARCH_MASK)


class TestOperandInit(unittest.TestCase):
    def test_init_imm(self) -> None:
        # test init with positive immediate number
        self.op = Operand("$0x32")
        self.assertEqual(self.op.type, OP_IMM)
        self.assertEqual(self.op.immediate_val, hex(0x32))
        self.assertEqual(self.op.registers, {})

    def test_init_label(self) -> None:
        # test init with label immediate number
        self.op = Operand("$S_0x804A018")
        self.assertEqual(self.op.type, OP_LBL)
        self.assertEqual(self.op.label, "S_0x804A018")
        self.assertEqual(self.op.registers, {})

    def test_init_label_data_sec(self) -> None:
        self.op = Operand("$S_0x804A018", data_sec=True)
        self.assertEqual(self.op.type, OP_LBL | OP_DEF)
        self.assertEqual(self.op.label, "S_0x804A018")
        self.assertEqual(self.op.registers, {})

    def test_init_label_without_perfix(self) -> None:
        self.op = Operand("S_0x804A018")
        self.assertEqual(self.op.type, OP_LBL)
        self.assertEqual(self.op.label, "S_0x804A018")
        self.assertEqual(self.op.registers, {})

    def test_init_label_without_perfix_deference(self) -> None:
        self.op = Operand("S_0x804A018", data_sec=True)
        self.assertEqual(self.op.type, OP_LBL | OP_DEF)
        self.assertEqual(self.op.label, "S_0x804A018")
        self.assertEqual(self.op.registers, {})

    def test_init_reg(self) -> None:
        self.op = Operand("%ebp")
        self.assertEqual(self.op.type, OP_REG)
        self.assertEqual(self.op.registers, {EBP: 1})

    def test_init_def(self) -> None:
        self.op = Operand("(%ebp)")
        self.assertEqual(self.op.type, OP_REG | OP_DEF)
        self.assertEqual(self.op.registers, {EBP: 1})
        self.assertEqual(self.op.is_deference(), True)

    def test_init_def_imm(self) -> None:
        self.op = Operand("0x32(%ebp)")
        self.assertEqual(self.op.type, OP_REG | OP_IMM | OP_DEF)
        self.assertEqual(self.op.immediate_val, hex(0x32))
        self.assertEqual(self.op.registers, {EBP: 1})
        self.assertEqual(self.op.is_deference(), True)

        self.op = Operand("-0xf4(%ebp)")
        self.assertEqual(self.op.type, OP_REG | OP_IMM | OP_DEF)
        self.assertEqual(self.op.immediate_val, hex(-0xf4))
        self.assertEqual(self.op.registers, {EBP: 1})
        self.assertEqual(self.op.is_deference(), True)

    def test_init_all(self) -> None:
        self.op = Operand("0x32(%ebp,%ecx,0x4)")
        self.assertEqual(self.op.type, OP_REG | OP_IMM | OP_DEF)
        self.assertEqual(self.op.immediate_val, hex(0x32))
        self.assertEqual(self.op.registers, {EBP: 1, ECX: 4})
        self.assertEqual(self.op.is_deference(), True)

        self.op = Operand("*-0xf4(%ebp,%esi,0x4)")
        self.assertEqual(self.op.type, OP_REG | OP_IMM | OP_DEF)
        self.assertEqual(self.op.immediate_val, hex(-0xf4))
        self.assertEqual(self.op.registers, {EBP: 1, ESI: 4})
        self.assertEqual(self.op.is_deference(), True)

        self.op = Operand("(,%esi,4)")
        self.assertEqual(self.op.type, OP_REG | OP_DEF)
        self.assertEqual(self.op.registers, {ESI: 4})
        self.assertEqual(self.op.is_deference(), True)

        self.op = Operand("0x0(,%eax,0x4)")
        self.assertEqual(self.op.type, OP_REG | OP_IMM | OP_DEF)
        self.assertEqual(self.op.immediate_val, hex(0x0))
        self.assertEqual(self.op.registers, {EAX: 4})
        self.assertEqual(self.op.is_deference(), True)

    def test_init_assert(self) -> None:
        with self.assertRaises(AssertionError):
            self.op = Operand("%aax")
        with self.assertRaises(AssertionError):
            self.op = Operand("%ebp,%aax")


class TestOperandSet(unittest.TestCase):
    def setUp(self) -> None:
        self.op = Operand()

    def test_set_default(self) -> None:
        self.op.set(type=OP_REG | OP_IMM | OP_DEF,
                    immediate_val=-32,
                    registers={RAX: 3, EBX: 2, AL: 1})
        self.assertEqual(self.op.type, 0b111)
        self.assertEqual(self.op.immediate_val, "-0x20")
        self.assertEqual(self.op.registers, {RAX: 3, EBX: 2, AL: 1})
        self.assertEqual(self.op.is_deference(), True)


class TestOperandGetVal(unittest.TestCase):
    def setUp(self) -> None:
        self.op = Operand()

    def test_operand_get_val_default(self) -> None:
        self.op.set(type=OP_REG | OP_IMM | OP_DEF,
                    immediate_val=-32,
                    registers={RAX: 3, EBX: 2, AL: 1})
        if ARCH_MASK == ARCH_X64:
            self.assertEqual(self.op.get_val(static_RTI),
                             "*(3*rax+2*get_exx(rbx)+get_lx(rax)-0x20)")
        else:
            with self.assertRaises(AssertionError):
                self.op.get_val(static_RTI)

    def test_operand_get_val_x86(self) -> None:
        self.op.set(type=OP_REG | OP_IMM | OP_DEF,
                    immediate_val=-32,
                    registers={EBX: 2, AL: 1})
        if ARCH_MASK == ARCH_X64:
            self.assertEqual(self.op.get_val(static_RTI),
                             "*(unsigned int *)(2*get_exx(rbx)+get_lx(rax)-0x20)")
        else:
            self.assertEqual(self.op.get_val(static_RTI),
                             "*(unsigned int *)(2*ebx+get_lx(eax)-0x20)")

    def test_operand_get_val_reg(self) -> None:
        self.op.set(type=OP_REG, immediate_val=None, registers={AL: 1})
        if ARCH_MASK == ARCH_X64:
            self.assertEqual(self.op.get_val(static_RTI), "get_lx(rax)")
        else:
            self.assertEqual(self.op.get_val(static_RTI), "get_lx(eax)")

    def test_operand_get_val_reg_bitcase(self) -> None:
        self.op.set(type=OP_REG | OP_IMM | OP_DEF,
                    immediate_val=0x10, registers={EBP: 1}, deference_type=MASK_L8_BIT)
        self.assertEqual(self.op.get_val(static_RTI),
                         "*(unsigned char *)(ebp+0x10)")

    def test_operand_get_val_imm(self) -> None:
        self.op.set(type=OP_IMM, immediate_val=32, registers=None)
        self.assertEqual(self.op.get_val(), "0x20")

    def test_operand_get_val_imm_neg(self) -> None:
        self.op.set(type=OP_IMM, immediate_val=-32, registers=None)
        self.assertEqual(self.op.get_val(), "-0x20")

    def test_operand_get_val_def(self) -> None:
        self.op.set(type=OP_REG | OP_DEF,
                    immediate_val=None,
                    registers={RAX: 3})

        if ARCH_MASK == ARCH_X64:
            self.assertEqual((self.op.get_val(static_RTI)),
                             "*(unsigned int *)(3*rax)")
        else:
            with self.assertRaises(AssertionError):
                self.op.get_val(static_RTI)

    def test_operand_get_val_label(self) -> None:
        # test init with label immediate number
        self.op.set(type=OP_LBL, registers=None, label="S_0x804A018")
        self.assertEqual(self.op.get_val(), "S_0x804A018")

    def test_operand_get_val_label_deference(self) -> None:
        # test init with label immediate number
        self.op.set(type=OP_LBL | OP_DEF, registers=None, label="S_0x804A018")
        self.assertEqual(self.op.get_val(), "*(unsigned int *)(S_0x804A018)")

    def test_operand_get_val_assert(self) -> None:
        self.op.set(type=OP_REG, immediate_val=None, registers={RAX: None})
        with self.assertRaises(AssertionError):
            self.op.get_val()
        with self.assertRaises(AssertionError):
            self.op.get_val(static_RTI)


class TestOperandStr(unittest.TestCase):
    def test_str_imm(self) -> None:
        # test init with positive immediate number
        self.op = Operand("$0x32")
        self.assertEqual(str(self.op), self.op.raw_string)

        # test init with label immediate number
        self.op = Operand("$S_0x804A018")
        self.assertEqual(str(self.op), self.op.raw_string)

    def test_str_reg(self) -> None:
        self.op = Operand("%ebp")
        self.assertEqual(str(self.op), self.op.raw_string)

    def test_str_def(self) -> None:
        self.op = Operand("(%ebp)")
        self.assertEqual(str(self.op), self.op.raw_string)

    def test_str_def_imm(self) -> None:
        self.op = Operand("0x32(%ebp)")
        self.assertEqual(str(self.op), self.op.raw_string)

        self.op = Operand("-0xf4(%ebp)")
        self.assertEqual(str(self.op), self.op.raw_string)

    def test_str_all(self) -> None:
        self.op = Operand("0x32(%ebp,%ecx,0x4)")
        self.assertEqual(str(self.op), self.op.raw_string)

        self.op = Operand("*-0xf4(%ebp,%esi,0x4)")
        self.assertEqual(str(self.op), self.op.raw_string)


class TestOperand(unittest.TestCase):
    def setUp(self):
        self.test_files = list()
        for path, dir_list, file_list in os.walk("../benchmark"):
            for file_name in file_list:
                self.test_files.append(os.path.join(path, file_name))

    def test_operand(self):
        for testcase in self.test_files:
            # skip suspicious test file `testfile2` for now
            if ('testfile2' in testcase) or ('.op' in testcase):
                continue
            with open(testcase)as f:
                for inst in f.read().split("\n"):
                    if inst == "" or inst.startswith("."):
                        continue
                    asm_info = util.split_inst(inst)

                    for operand_list in asm_info.values():
                        for operand in operand_list:
                            if ('ip' in operand):
                                print(operand)
                                with self.assertRaises(AssertionError):
                                    self.op = Operand(operand)
                            else:
                                op = Operand(operand)
                                self.assertEqual(str(op), operand)


if __name__ == "__main__":
    unittest.main()
