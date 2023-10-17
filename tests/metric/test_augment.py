import ast
import astor

from metric.complexity.transformer import *

class TestAugment:
    def test_parse(self):
        sample1 = "def foo():\n        for i in range(0, 5):\n            a=3\n        return a"

        module = ast.parse(sample1)
        func_node = module.body[0]
        new_node = LoopNodeTransformer().visit(func_node)
        print(astor.to_source(new_node))
