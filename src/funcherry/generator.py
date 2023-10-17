from metric.complexity.transformer import LoopNodeTransformer
from utils.augment import *

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