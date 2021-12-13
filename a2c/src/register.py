MASK_64_BIT = "rxx"
MASK_32_BIT = "exx"
MASK_16_BIT = "xx"
MASK_H8_BIT = "hx"
MASK_L8_BIT = "lx"


class Register:
    '''
        name: the name of the register, e.g., rax, rbx
        id: the id of actual register, e.g., eax.id == rax.id
        value_mask: indicates the avaliable bits, e.g., for eax is exx
    '''

    def __init__(self, name, id, arch_mask, value_mask=MASK_64_BIT):
        self.name = name
        self.id = id
        self.arch_mask = arch_mask
        self.value_mask = value_mask

    def __eq__(self, other):
        '''
            two Registers are equal only when they are from the same actual register
        '''
        return self.id == other.id

    def __le__(self, other):
        return self == other & self.value_mask <= other.value_mask

    def __or__(self, other):
        return self.id | other.id

    def __hash__(self):
        '''
            provide hash method, using only self.name
            which requires no repetitive reg name
        '''
        return hash(self.name)

    def get_mask_str(self):
        return "."+self.value_mask

    def is_base_reg(self):
        return self.arch_mask == self.value_mask

    def get_var_x64(self):
        if self.value_mask == MASK_64_BIT:
            return ["", ""]
        elif self.value_mask == MASK_32_BIT:
            return ["get_exx(", ")"]
        elif self.value_mask == MASK_16_BIT:
            return ["get_xx(", ")"]
        elif self.value_mask == MASK_H8_BIT:
            return ["get_hx(", ")"]
        elif self.value_mask == MASK_L8_BIT:
            return ["get_lx(", ")"]

    def get_var_x86(self):
        assert self.value_mask != MASK_64_BIT, "no rxx in arch x86."

        if self.value_mask == MASK_32_BIT:
            return ["", ""]
        elif self.value_mask == MASK_16_BIT:
            return ["get_xx(", ")"]
        elif self.value_mask == MASK_H8_BIT:
            return ["get_hx(", ")"]
        elif self.value_mask == MASK_L8_BIT:
            return ["get_lx(", ")"]

    def get_var(self):
        if self.arch_mask == MASK_64_BIT:
            return self.get_var_x64()
        else:
            return self.get_var_x86()
