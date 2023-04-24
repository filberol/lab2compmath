from functions.function import Function
import math

def_mul = math.pi/4.0
def_str = "pi/4"


class SinusFunction(Function):
    def __init__(self, mul=def_mul):
        Function.__init__(self)
        self.__mul = mul

    def value(self, x):
        return math.sin(x * self.__mul)

    def general_f(self, x, y):
        return self.value(x) - y

    def x_der(self, x):
        return math.pi / 4 * math.cos(x * math.pi / 4)

    def y_der(self, y):
        return -1

    def __str__(self):
        if self.__mul == def_mul:
            return f"sin(x * {def_str})"
        else:
            return f"sin(x * {self.__mul}"
