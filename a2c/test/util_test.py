from test_util import *
import util
import re
import os


class TestUtil(unittest.TestCase):

    def setUp(self):
        self.test_files = list()
        self.rep = re.compile(r"[ \t]+")
        for path, dir_list, file_list in os.walk("../benchmark"):
            for file_name in file_list:
                self.test_files.append(os.path.join(path, file_name))

    def test_split_inst(self):
        for testcase in self.test_files:
            with open(testcase) as f:
                for inst in f.read().split("\n"):
                    if inst == "" or inst.startswith("."):
                        continue
                    asm_info = util.split_inst(inst)
                    re_inst = list(asm_info.keys())[
                        0] + " " + ','.join(list(asm_info.values())[0])
                    self.assertEqual(self.rep.sub(
                        " ", inst, 0).strip(), re_inst.strip())

    def test_split_basicblocks(self):
        for testcase in self.test_files:
            if(not testcase.endswith(".s")):
                continue
            with open(testcase) as f:
                asm = f.read()
                bbs = util.split_basicblock(asm)
                self.assertEqual(len(bbs.keys()), asm.count(":\n"))

    def test_split_sections(self):
        for testcase in self.test_files:
            if(testcase.endswith(".s")):
                continue
            with open(testcase) as f:
                asm = f.read()
                secs = util.split_section(asm)
                self.assertEqual(len(secs.keys()), asm.count(".section"))


if __name__ == "__main__":
    unittest.main()
