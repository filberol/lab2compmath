from functions.function import Function
import math

def_mul1 = 2
def_mul2 = 0.5
def_const = -1


class ExpFunction(Function):
    def __init__(self, mul1=def_mul1, mul2=def_mul2, const=def_const ):
        Function.__init__(self)
        self.__mul1 = mul1
        self.__mul2 = mul2
        self.__const = const

    def value(self, x):
        return self.__mul1 * math.exp(-1 * abs(x * self.__mul2)) + self.__const

    def general_f(self, x, y):
        return self.value(x) - y

    def x_der(self, x):
        return -1 * x / (abs(x) * math.exp(abs(x) / 2))

    def y_der(self, y):
        return 1

    def __str__(self):
        return f"{self.__mul1} * e^-|{self.__mul2} x| {self.__const}"
