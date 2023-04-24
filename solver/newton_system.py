from solver.solver import SystemSolver
from solver.time_manager import time_count
from functions.function import Function
from matrix.matrix_solver import gauss_solve
from matrix.matrix import Matrix
from copy import deepcopy


class NewtonMethod(SystemSolver):

    __max_iterations = 1000

    @time_count
    def solve(self, func1: Function, func2: Function, coords, accuracy):
        # Starting values
        dyn_cords = deepcopy(coords)
        diff_x = coords[0] + 100
        diff_y = coords[1] + 100

        # Iteration
        iter_count = 0
        while abs(diff_x) > accuracy and abs(diff_y) > accuracy and iter_count < self.__max_iterations:
            iter_count += 1
            matrix = [
                [func1.x_der(dyn_cords[0]), func1.y_der(dyn_cords[1]), -1 * func1.general_f(dyn_cords[0], dyn_cords[1])],
                [func2.x_der(dyn_cords[0]), func2.y_der(dyn_cords[1]), -1 * func2.general_f(dyn_cords[0], dyn_cords[1])]
            ]
            result, errors = gauss_solve(Matrix(matrix))[1:3]
            diff_x = result[0]
            diff_y = result[1]
            dyn_cords[0] += result[0]
            dyn_cords[1] += result[1]
        return dyn_cords, iter_count

    def __str__(self):
        return "Newton's method"
