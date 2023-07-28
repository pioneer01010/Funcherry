import ast
import os
import re

from common.error import FunctionParseError
from pathlib import Path

class FunctionParser:

    def __init__(self, file_path):
        if not os.path.exists(file_path):
            cause = "No file exists '%s'", file_path
            raise FunctionParseError(cause=cause)

        self.file_path = file_path

    def parse_function_data(self):
        functions = {}
        with open(self.file_path, "r") as file:
            tree = ast.parse(file.read(), filename=self.file_path)

            # Define a visitor to visit FunctionDef nodes
            class FunctionNodeVisitor(ast.NodeVisitor):
                def visit_FunctionDef(self, node: ast.FunctionDef):
                    file.seek(0)
                    code_lines = file.readlines()
                    start_line = node.lineno - 1
                    end_line = node.end_lineno
                    code_block = "".join(code_lines[start_line: end_line])
                    return_annotation = ast.get_source_segment(code_lines[start_line: end_line]) if node.returns else ""
                    signature = {
                        "name": node.name,
                        "args": [arg.arg for arg in node.args.args],
                        "varargs": node.args.vararg and node.args.vararg.arg,
                        "kwonlyargs": [kwonly.arg for kwonly in node.args.kwonlyargs],
                        "kwarg": node.args.kwarg and node.args.kwarg.arg,
                        "return_annotation": return_annotation.strip()
                    }

                    # sig = "def " + node.name + "("
                    #
                    # for s in [arg.arg for arg in node.args.args]:
                    #     sig += s
                    #     sig += ","


                    functions[file.name + node.name] = node.name, signature, start_line, end_line, code_block
                    self.generic_visit(node)

            # Traverse the AST and extract function code blocks
            visitor = FunctionNodeVisitor()
            visitor.visit(tree)

        return functions

