from test_util import *
from define import *
from inst_template import FixInfo, InstTemplateGenerator


class TestInstTemplate(unittest.TestCase):

    def assertFixInfoListEqual(self, first, second) -> None:
        for k, fix_info in enumerate(first):
            self.assertEqual(fix_info.actions, second[k].actions)
            self.assertEqual(fix_info.use_type, second[k].use_type)
            self.assertEqual(fix_info.operand_idx, second[k].operand_idx)

    def test_inst_template_single(self) -> None:
        template_info = "mov op1,op2 >>>> long $op1*$ = $op2?$; $op2?$ = $op1?$; $rdi*$ = 100;$+$ = $op1?$;"
        template = InstTemplateGenerator(template_info)
        temp = template.templates[OPCODE_MOV]
        self.assertEqual(temp.opcode, 'mov')
        self.assertEqual(temp.operand_list, ['op1', 'op2'])
        self.assertEqual(
            temp.fix_template, 'long FIXME = FIXME; FIXME = FIXME; FIXME = 100;FIXME = FIXME;')

        self.assertFixInfoListEqual(
            temp.fix_info_list,
            [
                FixInfo(ACTION_NEW, USE_OP, 0),
                FixInfo(ACTION_EXIST, USE_OP, 1),
                FixInfo(ACTION_EXIST, USE_OP, 1),
                FixInfo(ACTION_EXIST, USE_OP, 0),
                FixInfo(ACTION_NEW, USE_REG, 16),
                FixInfo(ACTION_PUSH, USE_NONE, None),
                FixInfo(ACTION_EXIST, USE_OP, 0)
            ]
        )

    def test_inst_template_mov(self) -> None:
        mov_template = InstTemplateGenerator(
            "mov op1,op2 >>>> long $op1*$ = $op2?$;")
        temp = mov_template.templates[OPCODE_MOV]
        self.assertEqual(temp.opcode, 'mov')
        self.assertEqual(temp.operand_list, ['op1', 'op2'])
        self.assertEqual(temp.fix_template, 'long FIXME = FIXME;')
        self.assertFixInfoListEqual(
            temp.fix_info_list,
            [
                FixInfo(ACTION_NEW, USE_OP, 0),
                FixInfo(ACTION_EXIST, USE_OP, 1)
            ]
        )

    def test_inst_template_add(self) -> None:
        add_template = InstTemplateGenerator(
            "add op1,op2 >>>> long $op1*$ = $op1?$ + $op2?$;")
        temp = add_template.templates[OPCODE_ADD]
        self.assertEqual(temp.opcode, 'add')
        self.assertEqual(temp.operand_list, ['op1', 'op2'])
        self.assertEqual(temp.fix_template, 'long FIXME = FIXME + FIXME;')
        self.assertFixInfoListEqual(
            temp.fix_info_list,
            [
                FixInfo(ACTION_NEW, USE_OP, 0),
                FixInfo(ACTION_EXIST, USE_OP, 0),
                FixInfo(ACTION_EXIST, USE_OP, 1)
            ]
        )


if __name__ == "__main__":
    unittest.main()
