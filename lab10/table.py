def row_sums(matrix):
    return [sum(row) for row in matrix]


def column_sums(matrix):
    if not matrix:
        return []
    return [sum(row[column] for row in matrix) for column in range(len(matrix[0]))]


def diagonal_pattern(size):
    return [[0 if row == column else 1 if row < column else 2 for column in range(size)] for row in range(size)]


def transform(matrix):
    return [[0 if value < 0 else value for value in row] for row in matrix]
