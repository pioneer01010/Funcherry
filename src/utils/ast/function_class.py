import ast
import random

from utils.ast.variable import generate_variable, generate_variable_name
from utils.ast.expression import generate_expression, _generate_keyword


def generate_function_def(max_depth=None):
    from utils.ast.control_flow import generate_block

    name = generate_variable_name()
    args = _generate_arguments(max_depth=max_depth)
    body = generate_block(max_depth=max_depth)

    num_decorators = random.choice([0, 0, 0, 0, 0, 1, 1, 2])
    decorator_list = [generate_variable() for _ in range(num_decorators)]

    returns = random.choice([generate_variable()] + [None] * 4)

    return ast.FunctionDef(name, args, body, decorator_list, returns)

def _generate_arguments(max_depth=None):
    # normal arguments
    num_args = random.randrange(3)
    args = [_generate_arg() for _ in range(num_args)]
    defaults = [random.choice([generate_expression(max_depth=max_depth - 1)])
                for _ in range(random.randrange(num_args + 1))]

    # starred args and kwargs
    kwarg = random.choice([_generate_arg()] + [None] * 4)
    vararg = random.choice([_generate_arg()] + [None] * 4)

    # keyword-only arguments
    num_kwonlyargs = random.randrange(3)
    kwonlyargs = [_generate_arg() for _ in range(num_kwonlyargs)]
    kw_defaults = [random.choice([generate_expression(max_depth=max_depth - 1), None])
                   for _ in range(num_kwonlyargs)]

    return ast.arguments(args=args, vararg=vararg, kwonlyargs=kwonlyargs, kwarg=kwarg, defaults=defaults, kw_defaults=kw_defaults)


def _generate_arg(max_depth=None):
    name = generate_variable_name()
    annotation = random.choice([generate_variable()] + [None] * 4)
    return ast.arg(name, annotation)


def generate_class_def(max_depth=None):
    from utils.ast.control_flow import generate_block
    name = generate_variable_name()

    num_bases = random.choice([0, 0, 0, 1, 1, 2])
    bases = [generate_variable() for _ in range(num_bases)]

    keywords = []
    if random.choice([True, False, False, False, False]):
        value = generate_variable()
        keywords = [ast.keyword(arg='metaclass', value=value)]

    body = generate_block(max_depth=max_depth - 1)

    num_decorators = random.choice([0, 0, 0, 0, 0, 1, 1, 2])
    decorator_list = [generate_variable() for _ in range(num_decorators)]
    return ast.ClassDef(name, bases, keywords, body, decorator_list)


def generate_async_function_def(max_depth=None):
    from utils.ast.control_flow import generate_block

    name = generate_variable_name()
    args = _generate_arguments(max_depth=max_depth)
    body = generate_block(max_depth=max_depth)

    num_decorators = random.choice([0, 0, 0, 0, 0, 1, 1, 2])
    decorator_list = [generate_variable() for _ in range(num_decorators)]

    returns = random.choice([generate_variable()] + [None] * 4)

    return ast.AsyncFunctionDef(name, args, body, decorator_list, returns)