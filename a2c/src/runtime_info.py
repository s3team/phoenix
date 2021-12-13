from definition import *


class Stack(object):
    def __init__(self):
        self.content = list()

    def pop(self):
        return self.content.pop()

    def push(self, operand):
        self.content.append(operand)

    def access(self, idx):
        assert 0 < idx < len(self.content), "[Stack.access] bad idx"
        return self.content[-1-idx]


class RuntimeInfo(object):
    def __init__(self, stack=Stack(), reg_var_map={}, arch=ARCH_MASK):
        self.stack = stack

        if reg_var_map:
            self.reg_var_map = reg_var_map
        else:
            self.reg_var_map = dict()
            for reg in ALL_REG:
                if reg.is_base_reg():
                    self.reg_var_map[reg.id] = reg.name

    def get_var(self, reg):
        if reg.id in self.reg_var_map:
            return self.reg_var_map[reg.id]
        else:
            return None
