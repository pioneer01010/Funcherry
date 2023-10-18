import ast

class Complexity:    
    def calculate_cyclomatic(self, node: ast.FunctionDef):
        num_branches = 0
        num_loops = 0
        for child in ast.walk(node):
            if isinstance(child, ast.If) or isinstance(child, ast.While) or isinstance(child, ast.For):
                num_branches += 1
            elif isinstance(child, ast.Try) or isinstance(child, ast.ExceptHandler):
                num_branches += 1
        
        complexity = num_branches + num_loops + 1
        return complexity
    
    def calculate_call_depth(self, node: ast.FunctionDef):
        call_depth = 0
        def dfs(node, depth):
            nonlocal call_depth
            if isinstance(node, ast.Call):
                call_depth = max(call_depth, depth+1)
            for child in ast.iter_child_nodes(node):
                dfs(child, depth+1)
        dfs(node, 0)
        return call_depth