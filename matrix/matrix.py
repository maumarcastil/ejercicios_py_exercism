class Matrix:
    def __init__(self, matrix_string):
        m = matrix_string.split("\n")
        self.matrix = [[int(x) for x in y.split()] for y in m]

    def row(self, index):
        index = index - 1
        return self.matrix[index]

    def column(self, index):
        index = index - 1
        return [x[index] for x in self.matrix]