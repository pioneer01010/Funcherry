import ast
import astor

from metric.complexity.augmentator import *

class TestAugment:
    def test_parse(self):
        sample1 = "def foo():\n        for i in range(0, 5):\n            a=3\n        return a"

        module = ast.parse(sample1)
        func_node = module.body[0]
        transformer = AugmentForLoopTransformer(2)
        new_node = transformer.visit(func_node)
        print(astor.to_source(new_node))
