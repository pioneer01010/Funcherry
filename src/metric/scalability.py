import math
import ast

class Scalability:
    def calculate_halstead(self, node: ast.FunctionDef):
        ops = set()
        operands = set()
        for child in ast.walk(node):
            if isinstance(child, ast.operator):
                ops.add(type(child).__name__)
            elif isinstance(child, (ast.Name, ast.Constant)):
                operands.add(type(child).__name__)
        
        n1 = len(ops)
        n2 = len(operands)
        N1 = sum(1 for child in ast.walk(node) if isinstance(child, ast.operator))
        N2 = len(operands)

        N = N1 + N2
        n = n1 + n2
        if n == 0 or N == 0 or n1 == 0 or n2 == 0:
            return 0
        return (n1+n2) * math.log2(n1+n2) - (n1*math.log2(n1) + n2*math.log2(n2))
    
    def calculate_codeloc(self, node: ast.FunctionDef):
        return node.body[-1].lineno - node.body[0].lineno + 1