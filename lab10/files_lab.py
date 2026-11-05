def read_matrix(path):
    with open(path, encoding="utf-8") as file:
        lines = file.read().splitlines()
    if not lines:
        raise ValueError("Пустой файл")
    try:
        header = [int(part) for part in lines[0].split()]
    except ValueError:
        raise ValueError("Строка 1: размеры должны быть целыми числами")
    if len(header) != 2 or any(value <= 0 for value in header):
        raise ValueError("Строка 1: нужны два положительных размера")
    rows, columns = header
    if len(lines) != rows + 1:
        raise ValueError("Неверное количество строк таблицы")
    matrix = []
    for index, line in enumerate(lines[1:], 2):
        try:
            row = [int(part) for part in line.split()]
        except ValueError:
            raise ValueError(f"Строка {index}: ожидаются целые числа")
        if len(row) != columns:
            raise ValueError(f"Строка {index}: нужно {columns} чисел")
        matrix.append(row)
    return matrix


def selected_sum(matrix):
    return sum(value for row in matrix for value in row if value > 0)
