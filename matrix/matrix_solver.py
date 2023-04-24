from matrix.matrix import Matrix
import copy


def gauss_solve(matrix: Matrix):
    dims = matrix.dimension()
    result = gauss_triangle_extended(matrix)
    if count_determinant(matrix)[1] == 0.0:
        raise ValueError
    solution = [0] * dims
    errors = [0] * dims
    for var_n in range(dims - 1, -1, -1):
        # Write answer
        solution[var_n] = matrix.get_element(var_n, dims)
        # Remove known variables from answer
        for add_var in range(var_n + 1, dims):
            solution[var_n] -= matrix.get_element(var_n, add_var) * solution[add_var]
        # Remove multiplier
        solution[var_n] /= matrix.get_element(var_n, var_n)
    # Count errors
    for row in range(dims):
        err_sum = 0
        for var in range(dims):
            err_sum += matrix.get_element(row, var) * solution[var]
        errors[row] = abs(matrix.get_element(row, dims) - err_sum)
    return result, solution, errors


def count_determinant(matrix):
    local_matrix = copy.deepcopy(matrix)
    result = gauss_triangle_extended(local_matrix)
    mul = 1
    for diag in range(local_matrix.dimension()):
        mul *= local_matrix.get_element(diag, diag)
    del local_matrix
    if mul == -0.0:
        mul = 0.0
    return result, mul


def gauss_triangle_extended(matrix):
    for diagonal_index in range(matrix.dimension() - 1):
        # Find the row with the largest value in the current diagonal index
        max_row = diagonal_index
        max_value = abs(matrix.get_row(diagonal_index)[diagonal_index])
        for row in range(diagonal_index + 1, matrix.dimension()):
            value = abs(matrix.get_row(row)[diagonal_index])
            if value > max_value:
                max_row = row
                max_value = value
        # Eliminate values below the pivot in the current column
        for row in range(diagonal_index + 1, matrix.dimension()):
            factor = 0
            try:
                factor = matrix.get_row(row)[diagonal_index] / matrix.get_row(diagonal_index)[diagonal_index]
            except ZeroDivisionError:
                pass
            matrix.add_rows(row, diagonal_index, -factor)
    return matrix
