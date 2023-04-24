from functions.function import Function
import math

def_q_off = 2
def_const = 6
def_mul = 0.5


class PolFunction(Function):
    def __init__(self, q_off=def_q_off, const=def_const, mul=def_mul):
        Function.__init__(self)
        self.__q_off = q_off
        self.__const = const
        self.__mul = mul

    def value(self, x):
        return (-1 * (x + self.__q_off)**2 + x**3 + self.__const) * self.__mul

    def general_f(self, x, y):
        return self.value(x) - y

    def x_der(self, x):
        return -1 * x - 2 + 3/2 * x**2

    def y_der(self, y):
        return -1

    def __str__(self):
        return f"(x^3 - (x+{self.__q_off})^2 + {self.__const}) * {self.__mul}"
