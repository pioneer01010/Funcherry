# import ast
from ast import *
import astor
import random

from utils.ast.expression import generate_expression
from utils.ast.statement import generate_statement

def unparse(node):
    return astor.to_source(node)

def augment_for_node(node):
    target_ = generate_expression(1)
    iter_ = generate_expression(1)
    node = [For(target=target_, iter=iter_, body=node, orelse=[])]
    return node

def augment_while_node(node):
    test_ = generate_expression(1)
    node = [While(test=test_, body=node, orelse=[])]
    return node

def augment_if_node(node):
    test_ = generate_expression(1)
    if random.random() > 0.5:
        body_ = node
        orelse_ = generate_statement(1)
    else:
        body_ = generate_statement(1)
        orelse_ = node
    node = [If(test=test_, body=body_, orelse=orelse_)]
    return node