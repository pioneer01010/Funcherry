import ast
import os

from common.error import FunctionParseError
import logging


class FunctionNodeVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions = []
        self.classes = []

    def visit_ClassDef(self, node: ast.ClassDef):
        self.classes.append(node)
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.functions.append(node)
        self.generic_visit(node)


class FunctionParser:

    @classmethod
    def parse_functions_from_file(cls, filepath):
        if not os.path.exists(filepath):
            cause = "No file exists '%s'", filepath
            raise FunctionParseError(cause=cause)

        with open(filepath, "r", encoding='utf-8') as file:
            tree = ast.parse(file.read())
            file.seek(0)  # fp init
            source_code = file.readlines()

        visitor = FunctionNodeVisitor()
        visitor.visit(tree)

        functions = cls.parse_functions(visitor.functions, visitor.classes, file.name, source_code)

        return functions

    @classmethod
    def parse_functions(cls, fnodes, cnodes, filename, src):
        functions = []
        for node in fnodes:
            start = node.lineno - 1
            end = node.end_lineno
            code_block = "".join(src[start:end])
            return_annotation = ast.get_source_segment(src[start:end]) if node.returns else ""
            signature = {
                "name": node.name,
                "args": [arg.arg for arg in node.args.args],
                "varargs": node.args.vararg and node.args.vararg.arg,
                "kwonlyargs": [kwonly.arg for kwonly in node.args.kwonlyargs],
                "kwarg": node.args.kwarg and node.args.kwarg.arg,
                "return_annotation": return_annotation.strip()
            }
            clazz = cls._find_class_name(node, cnodes)
            sigstr = cls._to_str_signature(signature)

            functions.append({
                "file": filename,
                "class": clazz,
                "signature": sigstr,
                "start": start,
                "end": end,
                "block": code_block
            })

        return functions

    @classmethod
    def _find_class_name(cls, func_node: ast.FunctionDef, classes):
        for clz in classes:
            if func_node in clz.body:
                return clz.name
        # The function is not belonging any classes.
        return "None"

    @classmethod
    def _to_str_signature(cls, signature):
        signatures = signature["args"]
        if signature["varargs"] is not None:
            signatures.append(signature["varargs"])
        signatures += signature["kwonlyargs"]
        if signature["kwarg"] is not None:
            signatures.append(signature["kwarg"])

        sig_str = "def " + signature["name"] + "("
        for i in range(len(signatures)):
            sig_str += signatures[i]
            if i == len(signatures) - 1:
                break
            sig_str += ','
        sig_str += ")"

        return sig_str

