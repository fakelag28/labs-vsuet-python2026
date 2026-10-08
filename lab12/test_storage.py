"""Проверки хранения данных проекта «План учебных занятий» (работа 12).

Файлы создаются во временной папке, поэтому рабочий data.json не изменяется.
Запуск: python test_storage.py
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from logic import validate_records
from storage import load_records, save_records

RECORDS = [
    {"id": 1, "title": "Математика", "category": "учёба", "amount": 4, "completed": False},
    {"id": 2, "title": "Физика", "category": "учёба", "amount": 2, "completed": True},
]


def expect_exception(exception, action, description):
    """Проверить, что действие выбрасывает ожидаемое исключение."""
    try:
        action()
    except exception:
        pass
    else:
        assert False, f"Ошибка не обнаружена: {description}"


with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"

    # Отсутствующий файл.
    expect_exception(FileNotFoundError, lambda: load_records(path), "файла нет")

    # Сохранение и повторное чтение: структура и поля восстановлены.
    save_records(path, RECORDS)
    assert load_records(path) == RECORDS
    assert validate_records(load_records(path)) == RECORDS

    # Файл действительно JSON в UTF-8, кириллица читается.
    text = path.read_text(encoding="utf-8")
    assert "Математика" in text
    assert json.loads(text) == RECORDS

    # Пустой список.
    save_records(path, [])
    assert load_records(path) == []

    # Повреждённый JSON.
    path.write_text("{oops", encoding="utf-8")
    expect_exception(json.JSONDecodeError, lambda: load_records(path), "повреждённый JSON")

    # Неправильная кодировка.
    path.write_bytes(b'["\xff\xfe"]')
    expect_exception(UnicodeError, lambda: load_records(path), "файл не в UTF-8")

print("Проверки хранения пройдены")
