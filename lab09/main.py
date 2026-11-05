from table import column_sums, diagonal_pattern, row_sums, transform


def positive_integer(prompt):
    value = int(input(prompt))
    while value < 1:
        value = int(input("Введите положительное число: "))
    return value


def print_matrix(matrix):
    for row in matrix:
        print(*row)


def main():
    rows = positive_integer("Количество строк: ")
    columns = positive_integer("Количество столбцов: ")
    matrix = []
    for _ in range(rows):
        row = [int(part) for part in input("Строка таблицы: ").split()]
        while len(row) != columns:
            print(f"Нужно ровно {columns} чисел")
            row = [int(part) for part in input("Повторите строку: ").split()]
        matrix.append(row)
    print(f"Суммы строк: {row_sums(matrix)}")
    print(f"Суммы столбцов: {column_sums(matrix)}")
    print("Исходная таблица:")
    print_matrix(matrix)
    print("Новая таблица:")
    print_matrix(transform(matrix))
    size = positive_integer("Размер узора: ")
    print_matrix(diagonal_pattern(size))


if __name__ == "__main__":
    main()
