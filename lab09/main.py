"""Точка входа для лабораторной работы 9.

Программа читает прямоугольную таблицу, выводит суммы строк и столбцов,
затем строит диагональный узор и выводит исходную и преобразованную таблицы.
"""

from table import row_sums, column_sums, diagonal_pattern, transform


def read_matrix():
    """Прочитать прямоугольную таблицу с проверкой длины каждой строки."""
    rows = int(input("Количество строк: "))
    columns = int(input("Количество столбцов: "))
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    return matrix


def read_size():
    """Прочитать положительный размер квадратной таблицы."""
    size = int(input("Размер узора: "))
    while size < 1:
        print("Нужно положительное число")
        size = int(input("Размер узора: "))
    return size


def print_matrix(matrix):
    """Вывести таблицу по строкам, элементы разделены пробелами."""
    for row in matrix:
        print(*row)


def main():
    """Выполнить основной сценарий программы."""
    matrix = read_matrix()

    print("Суммы строк:", row_sums(matrix))
    print("Суммы столбцов:", column_sums(matrix))

    size = read_size()
    print("Диагональный узор:")
    print_matrix(diagonal_pattern(size))

    print("Исходная таблица:")
    print_matrix(matrix)

    print("Преобразованная таблица:")
    print_matrix(transform(matrix))


if __name__ == "__main__":
    main()
