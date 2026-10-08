"""Основная программа работы №10 «Текстовые файлы и обработка ошибок».

Программа запрашивает целое положительное число, затем читает таблицу из
matrix.txt, считает суммы строк и столбцов и записывает отчёт в report.txt.
Отчёт создаётся только после успешной проверки всех данных, поэтому при ошибке
чтения существующий report.txt остаётся без изменений.
"""
from pathlib import Path

from files_lab import read_matrix
from table import column_sums, row_sums

FOLDER = Path(__file__).resolve().parent
SOURCE = FOLDER / "matrix.txt"
REPORT = FOLDER / "report.txt"


def read_positive_integer():
    """Повторяет ввод, пока не получено целое число больше нуля.

    Для нечислового ввода и для неположительного числа выдаются разные
    сообщения.
    """
    while True:
        text = input("Введите целое положительное число: ")
        try:
            number = int(text)
        except ValueError:
            print("Это не целое число, повторите ввод")
            continue
        if number <= 0:
            print("Число должно быть больше нуля")
            continue
        return number


def selected_sum(matrix):
    """Вариант 1: сумма положительных элементов матрицы.

    Если подходящих элементов нет, результат равен нулю. Условие работает
    для любой прямоугольной матрицы.
    """
    total = 0
    for row in matrix:
        for value in row:
            if value > 0:
                total += value
    return total


def build_report(matrix):
    """Формирует текст отчёта по матрице."""
    lines = [
        "Суммы строк: " + " ".join(str(value) for value in row_sums(matrix)),
        "Суммы столбцов: " + " ".join(str(value) for value in column_sums(matrix)),
        "Результат варианта: " + str(selected_sum(matrix)),
    ]
    return "\n".join(lines) + "\n"


def main():
    """Точка входа: ввод числа, чтение файла, запись отчёта."""
    number = read_positive_integer()
    print("Принято число: " + str(number))

    try:
        matrix = read_matrix(SOURCE)
    except FileNotFoundError:
        print("Файл не найден: " + SOURCE.name)
        return
    except UnicodeError:
        print("Неверная кодировка: файл должен быть в UTF-8")
        return
    except ValueError as error:
        print("Ошибка формата данных: " + str(error))
        return
    except OSError as error:
        print("Ошибка доступа к файлу: " + str(error))
        return

    text = build_report(matrix)

    try:
        with open(REPORT, "w", encoding="utf-8", newline="\n") as file:
            file.write(text)
    except OSError as error:
        print("Не удалось записать отчёт: " + str(error))
        return

    print("Отчёт записан: " + REPORT.name)


if __name__ == "__main__":
    main()
