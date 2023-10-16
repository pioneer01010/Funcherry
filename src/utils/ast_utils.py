# import ast
from ast import *
import astor
import random

_AST_OP_NODES = (
    [And()], [Or()], [Eq()], [NotEq()], [Is()], [IsNot()], [In()], [NotIn()],
    [Lt()], [LtE()], [Gt()], [GtE()], [Add()], [Sub()], [Mult()], [Div()],
    [Mod()], [Pow()], [LShift()], [RShift()], [BitAnd()], [BitOr()], [BitXor()],
    [FloorDiv()], [Invert()], [Not()], [UAdd()], [USub()]
)

def unparse(node):
    return astor.to_source(node)

def augment_for_node(node):
    target_ = Name(id='i', ctx=Store())
    iter_ = Call(
        func = Name(id="range", ctx=Load()),
        args = [Num(n=5)],
        keywords=[]
    )
    node = [For(target=target_, iter=iter_, body=node, orelse=[])]
    return node

def augment_while_node(node):
    test_ = Compare(
        left = Name(id='i', ctx=Load()),
        ops=[random.choice(_AST_OP_NODES)],
        comparators=[Num(n=5)]
    )
    node = While(test=test_, body=node, orelse=[])
    return node