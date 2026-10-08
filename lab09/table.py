"""Работа с таблицами (вложенными списками).

Таблица представлена списком строк: matrix[row][column] — первый индекс
задаёт строку, второй — столбец. Функции модуля не выполняют ввод и вывод,
а только принимают и возвращают данные.
"""


def row_sums(matrix):
    """Вернуть список сумм строк таблицы.

    Для пустой таблицы возвращается пустой список.
    """
    sums = []
    for row in matrix:
        total = 0
        for value in row:
            total += value
        sums.append(total)
    return sums


def column_sums(matrix):
    """Вернуть список сумм столбцов прямоугольной таблицы.

    Для пустой таблицы возвращается пустой список. Непустая таблица
    прямоугольная и содержит хотя бы один столбец.
    """
    if not matrix:
        return []
    columns = len(matrix[0])
    sums = [0] * columns
    for row in matrix:
        for column in range(columns):
            sums[column] += row[column]
    return sums


def diagonal_pattern(size):
    """Построить квадратную таблицу размера size (size >= 1).

    На главной диагонали стоит 0, выше неё — 1, ниже неё — 2.
    """
    table = []
    for row in range(size):
        line = []
        for column in range(size):
            if row == column:
                line.append(0)
            elif row < column:
                line.append(1)
            else:
                line.append(2)
        table.append(line)
    return table


def transform(matrix):
    """Вернуть новую таблицу той же формы: отрицательные заменены нулями.

    Исходная таблица не изменяется. Для пустой таблицы — пустой список.
    """
    result = []
    for row in matrix:
        new_row = []
        for value in row:
            if value < 0:
                new_row.append(0)
            else:
                new_row.append(value)
        result.append(new_row)
    return result
