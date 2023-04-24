from solver.solver import FunctionSolver
from solver.time_manager import time_count
from functions.function import Function
from copy import deepcopy


class HalfSplitMethod(FunctionSolver):

    __max_iterations = 1000

    @time_count
    def solve(self, function: Function, borders, accuracy):
        if function.value(borders[0]) * function.value(borders[1]) > 0:
            raise ValueError(borders)

        # Starting values
        dyn_borders = deepcopy(borders)
        diff_x = dyn_borders[1] - dyn_borders[0]
        positive = function.value(borders[1]) > 0

        # Iteration process
        iter_count = 0
        while abs(diff_x) > accuracy and iter_count < self.__max_iterations:
            iter_count += 1
            diff_x = dyn_borders[1] - dyn_borders[0]
            new_x = sum(dyn_borders) / 2.0
            new_y = function.value(new_x)
            if new_y == 0:
                return new_x, iter_count
            if positive:
                if new_y > 0:
                    dyn_borders[1] = new_x
                else:
                    dyn_borders[0] = new_x
            else:
                if new_y > 0:
                    dyn_borders[0] = new_x
                else:
                    dyn_borders[1] = new_x
        return sum(dyn_borders) / 2.0, iter_count

    def __str__(self):
        return "Half split method"
