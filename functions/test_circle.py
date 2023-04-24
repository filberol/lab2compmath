from functions.function import Function


class TestCircle(Function):
    def __init__(self):
        Function.__init__(self)

    def general_f(self, x, y):
        return x**2 + y**2 - 4
