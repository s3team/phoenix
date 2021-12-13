from register import *


# x64 or x86
ARCH_X64 = MASK_64_BIT
ARCH_X86 = MASK_32_BIT
ARCH_MASK = ARCH_X86

# for Operand
OP_REG = 0x1
OP_IMM = 0x2
OP_DEF = 0x4
OP_LBL = 0x8

# for Opcode
# todo: should fix here later
OPCODE_START = 0x3


def gen_new_opcode():
    global OPCODE_START
    new_opcode = OPCODE_START
    OPCODE_START += 1
    return new_opcode


OPCODE_RET = 0x0
OPCODE_MOV = 0x1
OPCODE_ADD = 0x2
OPCODE_PUSH = 0x3
OPCODE_SUB = 0x4
OPCODE_JMP = 0x5
OPCODE_IMUL = 0x6
OPCODE_CMP = 0x7
OPCODE_JG = 0x8
OPCODE_LEAVE = 0x9
OPCODE_AND = 0xa
OPCODE_CALL = 0xb
OPCODE_HLT = 0xc

OPCODE_LEA = 0xd
OPCODE_JGE = 0xe
OPCODE_SHR = 0xf
OPCODE_SAR = 0x10
OPCODE_JLE = 0x11
OPCODE_XOR = 0x12
OPCODE_NOP = 0x13
OPCODE_JE = 0x14

OPCODE_MOVZBL = 0x15
OPCODE_MOVSBL = 0x16
OPCODE_JL = 0x17
OPCODE_POP = 0x18
OPCODE_MOVB = 0x19
OPCODE_JNE = 0x1a

opcode_map = {"mov": OPCODE_MOV, "ret": OPCODE_RET, "add": OPCODE_ADD, "push": OPCODE_PUSH, "pushl": OPCODE_PUSH,
              "sub": OPCODE_SUB, "movl": OPCODE_MOV, "jmp": OPCODE_JMP, "imul": OPCODE_IMUL, "addl": OPCODE_ADD,
              "subl": OPCODE_SUB, "cmpl": OPCODE_CMP, "jg": OPCODE_JG, "leave": OPCODE_LEAVE,
              "and": OPCODE_AND, "call": OPCODE_CALL, "cmp": OPCODE_CMP, "hlt": OPCODE_HLT,
              "lea": OPCODE_LEA, "jge": OPCODE_JGE, "shr": OPCODE_SHR, "sar": OPCODE_SAR, 
              "jle": OPCODE_JLE, "xor": OPCODE_XOR, "nop": OPCODE_NOP, "je": OPCODE_JE, "movzbl": OPCODE_MOVZBL,
              "movsbl": OPCODE_MOVSBL, "jl": OPCODE_JL, "pop": OPCODE_POP, "movb": OPCODE_MOVB, "jne": OPCODE_JNE}

invoke_opcodes = [opcode_map["call"]]
jmp_opcodes = [opcode_map["jmp"], opcode_map["jg"], opcode_map["jge"], opcode_map["jle"], opcode_map["je"], opcode_map["jl"], opcode_map["jne"]]
unconditional_branch_opcodes = [opcode_map["jmp"], opcode_map["hlt"], opcode_map["ret"]]
auto_cast_opcodes = [opcode_map["mov"]]
# for replace target type
USE_OP = 0x0
USE_REG = 0x1
USE_NONE = 0x2

# Define Register
BIT_RAX = 0x1
RAX = Register('rax', BIT_RAX, ARCH_MASK)
EAX = Register('eax', BIT_RAX, ARCH_MASK, MASK_32_BIT)
AX = Register('ax', BIT_RAX, ARCH_MASK, MASK_16_BIT)
AH = Register('ah', BIT_RAX, ARCH_MASK, MASK_H8_BIT)
AL = Register('al', BIT_RAX, ARCH_MASK, MASK_L8_BIT)

BIT_RBX = 0x2
RBX = Register('rbx', BIT_RBX, ARCH_MASK)
EBX = Register('ebx', BIT_RBX, ARCH_MASK, MASK_32_BIT)
BX = Register('bx', BIT_RBX, ARCH_MASK, MASK_16_BIT)
BH = Register('bh', BIT_RBX, ARCH_MASK, MASK_H8_BIT)
BL = Register('bl', BIT_RBX, ARCH_MASK, MASK_L8_BIT)

BIT_RCX = 0x4
RCX = Register('rcx', BIT_RCX, ARCH_MASK)
ECX = Register('ecx', BIT_RCX, ARCH_MASK, MASK_32_BIT)
CX = Register('cx', BIT_RCX, ARCH_MASK, MASK_16_BIT)
CH = Register('ch', BIT_RCX, ARCH_MASK, MASK_H8_BIT)
CL = Register('cl', BIT_RCX, ARCH_MASK, MASK_L8_BIT)

BIT_RDX = 0x8
RDX = Register('rdx', BIT_RDX, ARCH_MASK)
EDX = Register('edx', BIT_RDX, ARCH_MASK, MASK_32_BIT)
DX = Register('dx', BIT_RDX, ARCH_MASK, MASK_16_BIT)
DH = Register('dh', BIT_RDX, ARCH_MASK, MASK_H8_BIT)
DL = Register('dl', BIT_RDX, ARCH_MASK, MASK_L8_BIT)

BIT_RDI = 0x10
RDI = Register('rdi', BIT_RDI, ARCH_MASK)
EDI = Register('edi', BIT_RDI, ARCH_MASK, MASK_32_BIT)
DI = Register('di', BIT_RDI, ARCH_MASK, MASK_16_BIT)
DIL = Register('dil', BIT_RDI, ARCH_MASK, MASK_L8_BIT)

BIT_RBP = 0x20
RBP = Register('rbp', BIT_RBP, ARCH_MASK)
EBP = Register('ebp', BIT_RBP, ARCH_MASK, MASK_32_BIT)
BP = Register('bp', BIT_RBP, ARCH_MASK, MASK_16_BIT)
BPL = Register('bpl', BIT_RBP, ARCH_MASK, MASK_L8_BIT)

BIT_RSI = 0x40
RSI = Register('rsi', BIT_RSI, ARCH_MASK)
ESI = Register('esi', BIT_RSI, ARCH_MASK, MASK_32_BIT)
SI = Register('si', BIT_RSI, ARCH_MASK, MASK_16_BIT)
SIL = Register('sil', BIT_RSI, ARCH_MASK, MASK_L8_BIT)

BIT_RSP = 0x80
RSP = Register('rsp', BIT_RSP, ARCH_MASK)
ESP = Register('esp', BIT_RSP, ARCH_MASK, MASK_32_BIT)
SP = Register('sp', BIT_RSP, ARCH_MASK, MASK_16_BIT)
SPL = Register('spl', BIT_RSP, ARCH_MASK, MASK_L8_BIT)

BIT_R8 = 0x100
R8 = Register('r8', BIT_R8, ARCH_MASK)
R8D = Register('r8d', BIT_R8, ARCH_MASK, MASK_32_BIT)
R8W = Register('r8w', BIT_R8, ARCH_MASK, MASK_16_BIT)
R8B = Register('r8b', BIT_R8, ARCH_MASK, MASK_L8_BIT)

BIT_R9 = 0x200
R9 = Register('r9', BIT_R9, ARCH_MASK)
R9D = Register('r9d', BIT_R9, ARCH_MASK, MASK_32_BIT)
R9W = Register('r9w', BIT_R9, ARCH_MASK, MASK_16_BIT)
R9B = Register('r9b', BIT_R9, ARCH_MASK, MASK_L8_BIT)

BIT_R10 = 0x400
R10 = Register('r10', BIT_R10, ARCH_MASK)
R10D = Register('r10d', BIT_R10, ARCH_MASK, MASK_32_BIT)
R10W = Register('r10w', BIT_R10, ARCH_MASK, MASK_16_BIT)
R10B = Register('r10b', BIT_R10, ARCH_MASK, MASK_L8_BIT)

BIT_R11 = 0x1000
R11 = Register('r11', BIT_R11, ARCH_MASK)
R11D = Register('r11d', BIT_R11, ARCH_MASK, MASK_32_BIT)
R11W = Register('r11w', BIT_R11, ARCH_MASK, MASK_16_BIT)
R11B = Register('r11b', BIT_R11, ARCH_MASK, MASK_L8_BIT)

BIT_R12 = 0x2000
R12 = Register('r12', BIT_R12, ARCH_MASK)
R12D = Register('r12d', BIT_R12, ARCH_MASK, MASK_32_BIT)
R12W = Register('r12w', BIT_R12, ARCH_MASK, MASK_16_BIT)
R12B = Register('r12b', BIT_R12, ARCH_MASK, MASK_L8_BIT)

BIT_R13 = 0x4000
R13 = Register('r13', BIT_R13, ARCH_MASK)
R13D = Register('r13d', BIT_R13, ARCH_MASK, MASK_32_BIT)
R13W = Register('r13w', BIT_R13, ARCH_MASK, MASK_16_BIT)
R13B = Register('r13b', BIT_R13, ARCH_MASK, MASK_L8_BIT)

BIT_R14 = 0x8000
R14 = Register('r14', BIT_R14, ARCH_MASK)
R14D = Register('r14d', BIT_R14, ARCH_MASK, MASK_32_BIT)
R14W = Register('r14w', BIT_R14, ARCH_MASK, MASK_16_BIT)
R14B = Register('r14b', BIT_R14, ARCH_MASK, MASK_L8_BIT)

BIT_R15 = 0x10000
R15 = Register('r15', BIT_R15, ARCH_MASK)
R15D = Register('r15d', BIT_R15, ARCH_MASK, MASK_32_BIT)
R15W = Register('r15w', BIT_R15, ARCH_MASK, MASK_16_BIT)
R15B = Register('r15b', BIT_R15, ARCH_MASK, MASK_L8_BIT)

ALL_REG = [RAX, EAX, AX, AH, AL,
           RBX, EBX, BX, BH, BL,
           RCX, ECX, CX, CH, CL,
           RDX, EDX, DX, DH, DL,
           RDI, EDI, DI, DIL,
           RBP, EBP, BP, BPL,
           RSI, ESI, SI, SIL,
           RSP, ESP, SP, SPL,
           R8, R8D, R8W, R8B,
           R9, R9D, R9W, R9B,
           R10, R10D, R10W, R10B,
           R11, R11D, R11W, R11B,
           R12, R12D, R12W, R12B,
           R13, R13D, R13W, R13B,
           R14, R14D, R14W, R14B,
           R15, R15D, R15W, R15B]

reg_bit_map = dict()
reg_name_map = dict()
for reg in ALL_REG:
    reg_bit_map[reg.name] = reg.id
    reg_name_map[reg.name] = reg

# for replace action
ACTION_NEW = 0x1
ACTION_EXIST = 0x2
ACTION_POP = 0x4
ACTION_PUSH = 0x8
ACTION_NONE = 0x10
action_map = {"*": ACTION_NEW, "?": ACTION_EXIST,
              "-": ACTION_POP, "+": ACTION_PUSH}
