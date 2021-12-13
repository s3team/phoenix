from test_util import *
from loader import *
from util import split_section, split_basicblock
import os

c_flags = "-m32 -w -no-pie"


class TestLoader(unittest.TestCase):

    def test_loader(self) -> None:
        l = Loader('../template', '../benchmark/rawFac')
        # l = Loader('../template', '../benchmark/rawQsort')
        # l = Loader('../template', '../benchmark/rawReverse')
        l.translate_to_c()
        os.system("gcc {} output.c".format(c_flags))
        os.system("./a.out")

if __name__ == "__main__":
    unittest.main()
