from utils.augment import *

class Cyclomatic:
    
    def calculate(self, source_code):
        try:
            parsed_code = parse(source_code)            
            num_branches = 0
            num_loops = 0            
            for node in walk(parsed_code):
                if isinstance(node, If) or isinstance(node, While) or isinstance(node, For):
                    num_branches += 1
                elif isinstance(node, Try) or isinstance(node, ExceptHandler):
                    num_branches += 1
            
            complexity = num_branches + num_loops + 1            
            return complexity
        
        except SyntaxError:
            return -1