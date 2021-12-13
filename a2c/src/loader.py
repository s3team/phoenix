from define import *
from program_info import *
from builder import *
from util import *
from inst_template import InstTemplateGenerator

class Loader(object):
    def __init__(self, asm_file_path):
        self.sections = dict()
        self.GVlist = list()
        self.template = None
        self.cfile = str()
        self.load_template()
        self.load_asm_file(asm_file_path)

    def load_template(self):
        with open('../template/template_file') as f:
            template_content = f.read()
            self.template = InstTemplateGenerator(template_content)
        with open('../template/code_template.c') as f:
            self.cfile = f.read()

    def analyze_data_section(self, sec_name):
        label = str()
        values = list()
        is_ptr = False
        for line in self.sections[sec_name].split('\n'):
            if line.strip().endswith(":"):
                if label: self.GVlist.append(GlobalVariable(label,values,sec_name,is_ptr))
                label = line.split(":")[0]
                values = list()
                is_ptr = False
            else:
                m = re.search(r'\.([a-z]*) (0x[0-9a-f]*|S_0x[0-9A-F]*)', line)
                if m:
                    values.append(m.group(2))
                    if m.group(1) == 'long': is_ptr = True
        if label: self.GVlist.append(GlobalVariable(label,values,sec_name,is_ptr))
        

    def load_asm_file(self, asm_file_path):
        with open(asm_file_path) as f:
            asm_content = f.read()
        self.sections = split_section(asm_content)
        self.sections['.text'] = remove_redundant_code(self.sections['.text'], self.sections['.ctors'])
        self.GVlist = list()
        self.analyze_data_section('.rodata')
        self.analyze_data_section('.data')
        self.analyze_data_section('.bss')
        