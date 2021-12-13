from util import *
from program_info import *
from definition import *

class Builder(object):
    def __init__(self, asm):
        self.asm_program = asm
        pass
    
    def create_basicblocks(self):

        basicblocks = list()
        basicblocks_str_dict = split_basicblock(self.asm_program)
        for lable_name, insts in basicblocks_str_dict.items():
            basicblocks.append(BasicBlock(lable_name, insts))

        return basicblocks 

    def analyze_cfg(self, bbs_map):
        bb_name_list = list(bbs_map.keys())
        bb_count = len(bb_name_list)
        for idx in range(bb_count):
            bb = bbs_map[bb_name_list[idx]]
            if (bb.insts[-1].opcode in jmp_opcodes):
                succ_name = bb.insts[-1].operands[0].get_val()
                succ = bbs_map[succ_name]
                bb.successor.append(succ)
                succ.preceding.append(bb)
            
            if (idx < bb_count - 1) and (bb.insts[-1].opcode not in unconditional_branch_opcodes):
                succ_name = bb_name_list[idx+1]
                succ = bbs_map[succ_name]
                bb.successor.append(succ)
                succ.preceding.append(bb)


    def build_function(self, function, bb):
        for succ in bb.successor:
            if succ not in function.basicblocks:
                function.basicblocks.append(succ)
                self.build_function(function, succ)


    def build_program(self):
        bbs = list()
        bbs_map = dict()
        for bb_name, inst_list in split_basicblock(self.asm_program).items():
            bb = BasicBlock(bb_name, inst_list)
            bbs.append(bb)
            bbs_map[bb_name] = bb

        self.analyze_cfg(bbs_map)
        program = Program()
        for bb_name, bb in bbs_map.items():
            if len(bb.preceding) == 0:
                function = Function(bb, bb_name)
                program.funcs.append(function)
                function.basicblocks.append(bb)
                self.build_function(function, bb)
        
        # revert bb order to original order
        for func in program.funcs:
            ordered_bbs = list()
            for bb in bbs_map.values():
                if(bb in func.basicblocks):
                    ordered_bbs.append(bb)
            func.basicblocks = ordered_bbs

        return program
