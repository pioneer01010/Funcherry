import ast
import os

from common.error import FunctionParseError

class FunctionParser:

    def __init__(self, file_path):
        if not os.path.exists(file_path):
            cause = "No file exists '%s'", file_path
            raise FunctionParseError(cause=cause)

        self.file_path = file_path

    def get_function_code_blocks(self):
        function_code_blocks = {}

        with open(self.file_path, "r") as file:
            tree = ast.parse(file.read(), filename=self.file_path)

            # Define a visitor to visit FunctionDef nodes and extract function code blocks
            class FunctionCodeBlockVisitor(ast.NodeVisitor):
                def visit_FunctionDef(self, node: ast.FunctionDef):
                    file.seek(0)
                    code_lines = file.readlines()
                    code_block = "".join(code_lines[node.lineno - 1: node.end_lineno])
                    function_code_blocks[node.name] = code_block
                    self.generic_visit(node)

            # Traverse the AST and extract function code blocks
            visitor = FunctionCodeBlockVisitor()
            visitor.visit(tree)

        return function_code_blocks
