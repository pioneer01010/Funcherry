import ast
import os

from common.error import FunctionParseError
import logging

class FunctionParser:
    class Function:
        def __init__(self, file, start, end, signature, block):
            self.file = file
            self.start = start
            self.end = end
            self.signature = signature
            self.block = block
            logging.info(self.file + " | " + str(self.start) + " | " + str(self.end) + " | " + self.signature)

    @classmethod
    def from_file(cls, filepath):
        if not os.path.exists(filepath):
            cause = "No file exists '%s'", filepath
            raise FunctionParseError(cause=cause)

        with open(filepath, "r", encoding='utf-8') as file:
            tree = ast.parse(file.read(), filename=filepath)

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
                    self.generic_visit(node)
                    return cls.Function(file.name, start_line, end_line, cls._parse_function_signature(signature),
                                        code_block)

            visitor = FunctionNodeVisitor()
            visitor.visit(tree)

    @classmethod
    def _parse_function_signature(cls, signature):
        signatures = signature["args"]
        if signature["varargs"] is not None:
            signatures += signature["varargs"]
        signatures += signature["kwonlyargs"]
        if signature["kwarg"] is not None:
            signatures.append(signature["kwarg"])

        sig_str = "def " + signature["name"] + "("
        for i in range(len(signatures)):
            sig_str += signatures[i]
            if i == len(signatures)-1:
                break
            sig_str += ','
        sig_str += ")"

        return sig_str





