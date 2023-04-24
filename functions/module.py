from functions.function import Function

def_const = 1


class ModuleFunction(Function):
    def __init__(self, const=def_const):
        Function.__init__(self)
        self.__const = const

    def value(self, x):
        return -1 * abs(x) + self.__const

    def general_f(self, x, y):
        return self.value(x) - y

    def x_der(self, x):
        if x < 0:
            return 1
        else:
            return -1

    def y_der(self, y):
        return -1

    def __str__(self):
        return f"-|x| + {self.__const}"
