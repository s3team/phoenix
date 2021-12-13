from test_util import *
from definition import *
from inst_template import FixInfo, InstTemplateGenerator
from translator import Translator
from runtime_info import RuntimeInfo
from util import split_basicblock, split_inst
from program_info import *
from builder import *


class TestTranslator(unittest.TestCase):

    def test_translator(self) -> None:
        with open("../template/template_file") as f:
            template_content = f.read()

        # Construct Template
        template = InstTemplateGenerator(template_content)
        for k, v in template.templates.items():
            print(v)

        # Construct Runtime Info
        runtime_info = RuntimeInfo(arch=ARCH_MASK)

        # Construct Translator
        t = Translator(template.templates, None, runtime_info)

        # Construct Inst
        with open("../benchmark/Fac2.s") as f:
        #with open("../benchmark/qsort.s") as f:
        # with open("../benchmark/reverse.s") as f:
            asm = f.read()

        # Construct Builder and Program
        builder = Builder(asm)
        p = builder.build_program()

        ccode = t.translate_program(p)
        entry_point = "usermain()"
        ccode = ccode.replace("main()", entry_point)

        # Load into template.c
        with open("../template/code_template.c") as f:
            cfile = f.read()
            cfile = cfile.replace("__STACK_SIZE__", str(1024*1024*6))
            cfile = cfile.replace("__ENTRY_POINT__", entry_point)
            cfile = cfile.replace("__DISCOMPILATION_CODE__", ccode)

        with open("./output.c", "w") as f:
            f.write(cfile)


if __name__ == "__main__":
    unittest.main()
