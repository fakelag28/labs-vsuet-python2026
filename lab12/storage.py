"""Чтение и запись JSON для проекта «План учебных занятий» (работа 12).

Модуль не содержит консольных диалогов: о проблемах он сообщает исключениями.
Проверку структуры данных выполняет logic.validate_records().
"""

import json


def load_records(path):
    """Прочитать список записей из файла JSON в UTF-8.

    Выбрасывает FileNotFoundError, если файла нет, UnicodeError при
    неправильной кодировке и json.JSONDecodeError при повреждённом JSON.
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_records(path, records):
    """Записать список записей в файл JSON в UTF-8.

    При ошибке записи выбрасывает OSError, поэтому вызывающая сторона
    сообщает об успехе только после возврата из этой функции.
    """
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
        file.write("\n")
