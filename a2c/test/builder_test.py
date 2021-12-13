from test_util import *
from builder import *

import os

class TestBuilder(unittest.TestCase):

    def setUp(self):
        self.test_files = list()
        for path, dir_list, file_list in os.walk("../benchmark"):
            for file_name in file_list:
                self.test_files.append(os.path.join(path, file_name)) 

    def test_cfg(self):
        with open("../benchmark/qsort.s") as f:
            p = f.read()

        # Construct Builder
        builder = Builder(p)
        p = builder.build_program()

        # test the number of extracted functions
        self.assertEqual(len(p.funcs), 3)

        # test the order of functions
        # test the number of basicblocks for each function
        # test the order of basicblocks for each function
        self.assertEqual(p.funcs[0].func_name, "S_0x8048496")
        self.assertEqual(len(p.funcs[0].basicblocks), 1)
        self.assertEqual(p.funcs[0].basicblocks[0].name, "S_0x8048496")

        self.assertEqual(p.funcs[1].func_name, "qsort")
        self.assertEqual(len(p.funcs[1].basicblocks), 9)
        self.assertEqual(p.funcs[1].basicblocks[0].name, "qsort")
        self.assertEqual(p.funcs[1].basicblocks[1].name, "BB_27")
        self.assertEqual(p.funcs[1].basicblocks[2].name, "S_0x8048548")
        self.assertEqual(p.funcs[1].basicblocks[3].name, "BB_29")
        self.assertEqual(p.funcs[1].basicblocks[4].name, "S_0x8048583")
        self.assertEqual(p.funcs[1].basicblocks[5].name, "S_0x8048587")
        self.assertEqual(p.funcs[1].basicblocks[6].name, "BB_32")
        self.assertEqual(p.funcs[1].basicblocks[7].name, "S_0x80485D2")
        self.assertEqual(p.funcs[1].basicblocks[8].name, "S_0x80485D3")

        self.assertEqual(p.funcs[2].func_name, "main")
        self.assertEqual(len(p.funcs[2].basicblocks), 1)
        self.assertEqual(p.funcs[2].basicblocks[0].name, "main")

        
if __name__ == "__main__":
    unittest.main()