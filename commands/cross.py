from commands.command import Command
from terminal_colors import *
from solver import newton_system


class CrossFunctions(Command):
    def __init__(self, manager):
        Command.__init__(self, manager)

    __def_accuracy = 0.00001

    # args:
    # 1 - function number
    # 2 - function number
    # 3 - start cords x_0:y_0
    # 4 - accuracy
    def execute_command(self, arguments):
        if len(arguments) < 3:
            print_c(
                f"Usage: -> cross <function No> <function No> <x_0>:<y_0> <accuracy(default {self.__def_accuracy})>",
                Colors.WARNING
            )
            return
        if int(arguments[0]) + int(arguments[1]) > len(self.state_manager.get_functions()) * 2\
                or any(map(lambda x: int(x), arguments[:2])) <= 0:
            print_c("Invalid function index!", Colors.FAIL)
            return

        try:
            functions = self.state_manager.get_functions()
            cords = list(map(lambda x: float(x), arguments[2].split(":")))
            func1 = functions[int(arguments[0]) - 1]
            func2 = functions[int(arguments[1]) - 1]
            accuracy = float(arguments[3]) if len(arguments) > 3 else self.__def_accuracy
        except ValueError:
            print_c("Wrong arguments!", Colors.FAIL)
            return

        try:
            method = newton_system.NewtonMethod()
            answer = method.solve(func1, func2, cords, accuracy)
            print(f"{method}: x={answer[0][0]} y={answer[0][1]} with accuracy of {accuracy}, {answer[1]} iterations")
        except ValueError:
            print_c("No solutions on interval, or function only touching null", Colors.FAIL)
        except ZeroDivisionError:
            print_c("No continuous derivative around coordinates", Colors.FAIL)
        except OverflowError:
            print_c("Overflow error", Colors.FAIL)
