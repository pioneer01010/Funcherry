class A:
    def a_func1(self):
        pass

    class B:
        def __init__(self):
            self.b_num = 1
            self.b_list = []

        def b_func1(self):
            pass

        def b_func2(self, param1, param2, param3):
            pass

        def b_func3(self):
            return self.b_list

    def a_func2(self, param1):
        pass

    @classmethod
    def a_func3(cls):
        pass
