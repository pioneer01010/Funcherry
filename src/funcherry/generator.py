from metric.complexity.augment import LoopNodeTransformer
from utils.ast_utils import *

class Generator:

    @staticmethod
    def gen_positive(anchor):
        positive = ""
        return positive
    
    @staticmethod
    def gen_negatives(anchor):
        negatives = []
        func_node = parse(anchor).body[0]
        loop_negative = LoopNodeTransformer().visit(func_node)
        negatives.append(unparse(loop_negative))
        return negatives