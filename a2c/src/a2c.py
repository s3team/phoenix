import os
from argparse import RawTextHelpFormatter, ArgumentParser

from loader import *
from translator import *
from runtime_info import *
from builder import *
from define import *

c_flags = "-w -no-pie"

def translate_to_c(asm_info, template, cfile, arch, output_file):
    # Construct Runtime Info
    runtime_info = RuntimeInfo(arch=ARCH_X64 if arch == '__x64__' else ARCH_X86)

    # Construct Translator
    t = Translator(template.templates, None, runtime_info)

    # Construct Builder and Program
    builder = Builder(asm_info.sections['.text'])
    p = builder.build_program()

    ccode = t.translate_program(p, asm_info.GVlist)
    entry_point = "usermain()"
    ccode = ccode.replace("main()", entry_point)

    cfile = cfile.replace("__ARCH_INFO__", arch)
    cfile = cfile.replace("__STACK_SIZE__", str(1024*1024*6))
    cfile = cfile.replace("__ENTRY_POINT__", entry_point)
    cfile = cfile.replace("__DISCOMPILATION_CODE__", ccode)
    
    with open(output_file, "w") as f:
        f.write(cfile)

if __name__ == "__main__":
    p = ArgumentParser(formatter_class=RawTextHelpFormatter)
    p.add_argument('asm_file', help='path to the input asm file which should be generated by Uroboros')
    p.add_argument('-a', '--arch', help='specify the architecture of the input asm file (x86/x64), x86 by default', default='x86')
    p.add_argument('-o', '--output', help='specify the name of output C file', default='output')
    p.add_argument('-v', '--version', action='version', version='A2cend 0.1')

    args = p.parse_args()
    asm_file = args.asm_file
    arch = '__' + args.arch + '__'
    output_file = args.output + '.c'

    l = Loader(asm_file)
    translate_to_c(l, l.template, l.cfile, arch, output_file)

    print("processing succeeded")

    if arch == '__x86__': c_flags += ' -m32'

    os.system("gcc {} output.c".format(c_flags))
    # os.system("./a.out")    
