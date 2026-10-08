"""Проверки чтения матрицы из файла (работа №10).

Проверки создают файлы в отдельной временной папке tempfile.TemporaryDirectory.
"""
from pathlib import Path
from tempfile import TemporaryDirectory

from files_lab import read_matrix

def read_from_text(directory, text):
    """Записывает текст во временный файл matrix.txt и читает из него матрицу."""
    path = Path(directory) / "matrix.txt"
    path.write_text(text, encoding="utf-8")
    return read_matrix(path)

def main():
    """Выполняет все проверки чтения матрицы."""
    with TemporaryDirectory() as directory:
        assert read_from_text(directory, "1 2\n7 -1\n") == [[7, -1]]

        assert read_from_text(directory, "1 1\n0\n") == [[0]]

        try:
            read_from_text(directory, "")
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена"

        try:
            read_from_text(directory, "0 3\n")
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена"

        try:
            read_from_text(directory, "1 2\n1\n")
        except ValueError as error:
            assert "Строка 2" in str(error), "Нет номера строки: " + str(error)
        else:
            assert False, "Ошибка не обнаружена"

        try:
            read_from_text(directory, "1 2\n1 x\n")
        except ValueError as error:
            assert "Строка 2" in str(error), "Нет номера строки: " + str(error)
        else:
            assert False, "Ошибка не обнаружена"

        try:
            read_from_text(directory, "1 1\n5\n6\n")
        except ValueError:
            pass
        else:
            assert False, "Ошибка не обнаружена"

        missing = Path(directory) / "no_such_file.txt"
        try:
            read_matrix(missing)
        except FileNotFoundError:
            pass
        else:
            assert False, "Ошибка не обнаружена"

    print("Все проверки чтения матрицы пройдены")

if __name__ == "__main__":
    main()
