import ast
import random

from utils.ast.words import generate_word
from utils.ast.variable import generate_variable

MAX_LIST_LENGTH = 3

def generate_num(max_depth=None):
    n = random.randrange(10)
    return ast.Num(n)

def generate_string(max_depth=None):
    return ast.Str(generate_word())

def generate_formatted_value(max_depth=None):
    var = generate_variable()
    conversion = -1
    format_spec = None
    return ast.FormattedValue(var, conversion, format_spec)

def generate_joined_string(max_depth=None):
    length = random.randrange(MAX_LIST_LENGTH)
    values = []
    for _ in range(length):
        if 0 == random.randrange(2):
            string_part = generate_string(max_depth=max_depth)
        else:
            string_part = generate_formatted_value(max_depth=max_depth)
        values.append(string_part)
        values.append(ast.Str(" "))
    return ast.JoinedStr(values)

def generate_bytes(max_depth=None):
    seq = generate_word().encode('utf-8')
    return ast.Bytes(seq)

def generate_ellipsis(max_depth=None):
    return ast.Ellipsis()

def generate_name_constant(max_depth=None):
    constant = random.choice([True, False, None])
    return ast.NameConstant(constant)

def generate_list(max_depth=None):
    from utils.ast.expression import generate_expression
    length = random.randrange(MAX_LIST_LENGTH)
    elts = [generate_expression(max_depth=max_depth - 1) for _ in range(length)]
    return ast.List(elts, ast.Load())

def generate_tuple(max_depth=None):
    from utils.ast.expression import generate_expression
    length = random.randrange(MAX_LIST_LENGTH)
    elts = [generate_expression(max_depth=max_depth - 1) for _ in range(length)]
    return ast.Tuple(elts, ast.Load())

def generate_set(max_depth=None):
    from utils.ast.expression import generate_expression
    length = random.randrange(MAX_LIST_LENGTH)
    elts = [generate_expression(max_depth=max_depth - 1) for _ in range(length)]
    return ast.Set(elts)

def generate_dict(max_depth=None):
    from utils.ast.expression import generate_expression
    length = random.randrange(MAX_LIST_LENGTH)
    keys = [generate_expression(max_depth=max_depth - 1) for _ in range(length)]
    values = [generate_expression(max_depth=max_depth - 1) for _ in range(length)]
    return ast.Dict(keys, values)

def generate_literal(max_depth=None):
    flat_choices = [
        generate_num,
        generate_string,
        generate_joined_string,
        generate_bytes,
        generate_ellipsis,
        generate_name_constant,
    ]

    complex_choices = [
        generate_list,
        generate_tuple,
        generate_set,
        generate_dict,
    ]

    if max_depth >= 1:
        choices = flat_choices + complex_choices
    else:
        choices = flat_choices

    return random.choice(choices)(max_depth=max_depth)