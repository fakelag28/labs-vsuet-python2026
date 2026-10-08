"""Чтение таблицы целых чисел из текстового файла (работа №10).

Модуль содержит функцию read_matrix, которая читает файл в кодировке UTF-8
и проверяет его формат, сообщая об ошибках через исключение ValueError.
"""

def read_matrix(path):
    """Читает прямоугольную матрицу целых чисел из текстового файла.

    Формат файла:
    - первая строка: два положительных целых числа — количество строк и столбцов;
    - далее ровно указанное число строк, в каждой ровно указанное число целых чисел.

    Лишние и пустые строки считаются ошибкой. Один обычный перевод строки после
    последней строки данных допустим.

    При ошибке формата выбрасывает ValueError с понятным пояснением и номером
    строки, если он применим. Возвращает список списков целых чисел.
    """
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if len(lines) == 0:
        raise ValueError("Файл пуст: отсутствует строка с размерами")

    header = lines[0].split()
    if len(header) != 2:
        raise ValueError(
            "Строка 1: ожидалось два целых числа (строки и столбцы), "
            "получено " + str(len(header))
        )

    try:
        rows = int(header[0])
        columns = int(header[1])
    except ValueError:
        raise ValueError("Строка 1: размеры должны быть целыми числами")

    if rows <= 0 or columns <= 0:
        raise ValueError("Строка 1: размеры должны быть положительными")

    matrix = []
    for index in range(rows):
        line_number = index + 2
        if line_number > len(lines):
            raise ValueError(
                "Строка " + str(line_number) + ": ожидалось " + str(columns)
                + " чисел, но строка отсутствует"
            )

        text = lines[line_number - 1]
        if text.strip() == "":
            raise ValueError(
                "Строка " + str(line_number) + ": пустая строка недопустима"
            )

        parts = text.split()
        if len(parts) != columns:
            raise ValueError(
                "Строка " + str(line_number) + ": ожидалось " + str(columns)
                + " чисел, получено " + str(len(parts))
            )

        row = []
        for part in parts:
            try:
                row.append(int(part))
            except ValueError:
                raise ValueError(
                    "Строка " + str(line_number) + ": «" + part
                    + "» не является целым числом"
                )
        matrix.append(row)

    used = 1 + rows
    if len(lines) > used:
        raise ValueError(
            "Строка " + str(used + 1) + ": лишние строки после данных"
        )

    return matrix
