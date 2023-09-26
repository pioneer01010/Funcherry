import ast

class Cyclomatic:
    
    def calculate(self, source_code):
        try:
            parsed_code = ast.parse(source_code)
            
            num_branches = 0
            num_loops = 0
            
            for node in ast.walk(parsed_code):
                if isinstance(node, ast.If) or isinstance(node, ast.While) or isinstance(node, ast.For):
                    num_branches += 1
                elif isinstance(node, ast.Try) or isinstance(node, ast.ExceptHandler):
                    num_branches += 1
            
            complexity = num_branches + num_loops + 1
            
            return complexity
        
        except SyntaxError:
            return -1