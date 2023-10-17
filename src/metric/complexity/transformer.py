import random

from utils.augment import *

class LoopNodeTransformer(NodeTransformer):
    def visit_For(self, node):
        node.body = LoopNodeAugment(random.randint(1,3)).transform(node.body)
        return node
    
class LoopNodeAugment:
    def __init__(self, cnt):
        self.cnt = cnt
    
    def transform(self, node):
        for i in range(self.cnt):
            augment = random.choice([augment_for_node, augment_while_node, augment_if_node])
            node = augment(node)
        return node