import ast

from metric.complexity import Complexity
from metric.scalability import Scalability

sample1 = "def calculate_cyclomatic(self, node: ast.FunctionDef):\n        num_branches = 0\n        num_loops = 0\n        for child in ast.walk(node):\n            if isinstance(node, ast.If) or isinstance(node, ast.While) or isinstance(node, ast.For):\n                num_branches += 1\n            elif isinstance(node, ast.Try) or isinstance(node, ast.ExceptHandler):\n                num_branches += 1\n        \n        complexity = num_branches + num_loops + 1\n        return complexity"
node = ast.parse(sample1).body[0]

class TestCalculateMetric:

    def test_calculate_cyclomatic(self):
        val = Complexity().calculate_cyclomatic(node)
        print("Cyclomatic: ", val)
    
    def test_calculate_call_depth(self):
        val = Complexity().calculate_call_depth(node)
        print("Call Depth: ", val)
    
    def test_calculate_halstead(self):
        val = Scalability().calculate_halstead(node)
        print("Halstead: ", val)
    
    def test_calculate_codeloc(self):
        val = Scalability().calculate_codeloc(node)
        print("CodeLOC: ", val)