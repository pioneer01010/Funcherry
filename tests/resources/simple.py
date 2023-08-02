class A:
    def __init__(self):
        self.a = 1
        self.b = 2

    def a_func1(self):
        return self.a

    def a_func2(self):
        return self.b


def arg_test_func(*args):
    print("Arguments test case: " + args[0])


def kwarg_test_func(**kargs):
    print("Keyword arguments test case: " + kargs["none"])


def arguments_test_func(arg, *args, kwonly, **kwargs):
    print('arg:', arg)
    print('args:', args)
    print('kwonly:', kwonly)
    print('kwargs:', kwargs)
