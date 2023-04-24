from solver.solver import FunctionSolver
from solver.time_manager import time_count
from copy import deepcopy
from functions.function import Function


class ChordMethod(FunctionSolver):

    __max_iterations = 1000

    @time_count
    def solve(self, function: Function, borders, accuracy):
        if function.value(borders[0]) * function.value(borders[1]) > 0:
            raise ValueError(borders)

        #     x = a - (b - a)f(a) / (f(b) - f(a))
        dyn_borders = deepcopy(borders)
        diff_x = dyn_borders[1] - dyn_borders[0]
        positive = function.value(borders[1]) > 0

        # Iteration process
        iter_count = 0
        while abs(diff_x) > 0 and iter_count < self.__max_iterations:
            iter_count += 1
            diff_x = dyn_borders[1] - dyn_borders[0]
            f_a = function.value(borders[0])
            f_b = function.value(borders[1])
            new_x = borders[0] - (borders[1] - borders[0]) / (f_b - f_a) * f_a
            new_y = function.value(new_x)
            if new_y == 0:
                return new_x, iter_count
            if positive:
                if new_y < 0:
                    borders[0] = new_x
                else:
                    borders[1] = new_x
            else:
                if new_y < 0:
                    borders[1] = new_x
                else:
                    borders[0] = new_x
        return sum(dyn_borders) / 2.0, iter_count

    def __str__(self):
        return "Chords method"
