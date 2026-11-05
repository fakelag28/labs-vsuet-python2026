from pathlib import Path
from files_lab import read_matrix, selected_sum
from table import column_sums, row_sums


def read_positive_integer():
    while True:
        try:
            value = int(input("Положительное целое число: "))
            if value > 0:
                return value
            print("Число должно быть больше нуля")
        except ValueError:
            print("Не целое число")


def main():
    read_positive_integer()
    directory = Path(__file__).resolve().parent
    try:
        matrix = read_matrix(directory / "matrix.txt")
        rows = " ".join(map(str, row_sums(matrix)))
        columns = " ".join(map(str, column_sums(matrix)))
        report = f"Суммы строк: {rows}\nСуммы столбцов: {columns}\nРезультат варианта: {selected_sum(matrix)}\n"
        (directory / "report.txt").write_text(report, encoding="utf-8")
        print("Отчёт сохранён")
    except FileNotFoundError:
        print("Файл не найден")
    except UnicodeError as error:
        print(f"Ошибка кодировки: {error}")
    except ValueError as error:
        print(f"Ошибка формата: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
