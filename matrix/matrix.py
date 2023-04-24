class Matrix:
    def __init__(self, matrix=None):
        if matrix is None:
            matrix = [[]]
        self.__matrix = matrix

    def get_matrix(self):
        return self.__matrix

    def dimension(self):
        return len(self.__matrix)

    def get_element(self, row, column):
        return self.__matrix[row][column]

    def set_element(self, row, column, value):
        self.__matrix[row][column] = value

    def get_row(self, row):
        return self.__matrix[row]

    def swap_rows(self, row1, row2):
        self.__matrix[row1], self.__matrix[row2] = self.__matrix[row2], self.__matrix[row1]

    def add_rows(self, dest_row, src_row, factor):
        for ind in range(len(self.__matrix[dest_row])):
            self.__matrix[dest_row][ind] += self.__matrix[src_row][ind] * factor

    def is_empty(self):
        if not self.__matrix or not self.__matrix[0]:
            return True
        else:
            return False

    def __str__(self):
        if self.is_empty():
            return "Matrix is empty!"
        else:
            string = ""
            for row in self.__matrix:
                row_string = "["
                for elem in row:
                    row_string += f"{elem:.2f} "
                row_string += "]\n"
                string += row_string
            return string[:len(string) - 1]
