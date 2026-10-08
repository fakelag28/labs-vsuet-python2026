"""Проверки анализа набора задач (лабораторная работа 11).

Сетевые вызовы здесь не выполняются: модуль fetch_profile не импортируется.
Запуск: python test_analysis.py
"""

import json
from pathlib import Path
from tempfile import TemporaryDirectory

from analysis import completion_counts, select_tasks, top_users, validate_todos
from main import save_json

TODOS = [
    {"id": 1, "userId": 5, "title": "Ввод", "completed": True},
    {"id": 2, "userId": 5, "title": "Циклы", "completed": False},
    {"id": 3, "userId": 10, "title": "Строки", "completed": True},
    {"id": 4, "userId": 10, "title": "Файлы", "completed": True},
    {"id": 5, "userId": 5, "title": "Списки", "completed": True},
]

def ids(records):
    """Вернуть идентификаторы записей списком."""
    return [record["id"] for record in records]

def expect_value_error(action, description):
    """Проверить, что действие выбрасывает ValueError."""
    try:
        action()
    except ValueError:
        pass
    else:
        assert False, f"Ошибка не обнаружена: {description}"

def check_root_not_list():
    """Корень данных не список."""
    validate_todos({"id": 1})

def check_record_not_dict():
    """Запись не является объектом."""
    validate_todos(["строка"])

def check_duplicate_id():
    """Идентификатор записи повторяется."""
    validate_todos([
        {"id": 1, "userId": 1, "title": "A", "completed": True},
        {"id": 1, "userId": 2, "title": "B", "completed": False},
    ])

def check_missing_user_id():
    """В записи отсутствует ключ userId."""
    validate_todos([{"id": 1, "title": "A", "completed": True}])

def check_completed_is_string():
    """Поле completed передано строкой."""
    validate_todos([{"id": 1, "userId": 1, "title": "A", "completed": "false"}])

def check_id_is_bool():
    """Идентификатор передан логическим значением."""
    validate_todos([{"id": True, "userId": 1, "title": "A", "completed": True}])

def check_id_not_positive():
    """Идентификатор не является положительным."""
    validate_todos([{"id": 0, "userId": 1, "title": "A", "completed": True}])

def check_empty_title():
    """Название состоит из пробелов."""
    validate_todos([{"id": 1, "userId": 1, "title": "   ", "completed": True}])

counts = completion_counts(TODOS)
assert counts == {5: 2, 10: 2}, counts
assert top_users(counts) == [5, 10], top_users(counts)
leaders = top_users(counts)
saved = [record for record in TODOS if record["completed"] and record["userId"] in leaders]
assert ids(saved) == [1, 3, 4, 5], ids(saved)

assert completion_counts([]) == {}
assert top_users({}) == []
only_open = [{"id": 1, "userId": 7, "title": "Тест", "completed": False}]
assert top_users(completion_counts(only_open)) == []

assert top_users({1: 0, 2: 1, 3: 0}) == [2]
assert top_users({1: 3, 2: 3, 3: 1}) == [1, 2]

assert ids(select_tasks(TODOS, 5)) == [1, 2, 5], ids(select_tasks(TODOS, 5))
assert select_tasks(TODOS, 99) == []
assert select_tasks(TODOS, 5, None) == select_tasks(TODOS, 5)

before = [record.copy() for record in TODOS]
select_tasks(TODOS, 5)
completion_counts(TODOS)
top_users(completion_counts(TODOS))
assert TODOS == before, "Исходные записи изменены"

assert validate_todos(TODOS) == TODOS
assert validate_todos([]) == []
assert validate_todos([{"id": 1, "userId": 2, "title": "Т", "completed": True, "extra": 5}])

expect_value_error(check_root_not_list, "корень не список")
expect_value_error(check_record_not_dict, "запись не словарь")
expect_value_error(check_duplicate_id, "повторный id")
expect_value_error(check_missing_user_id, "отсутствующий userId")
expect_value_error(check_completed_is_string, "completed строкой")
expect_value_error(check_id_is_bool, "id = True")
expect_value_error(check_id_not_positive, "id не положительный")
expect_value_error(check_empty_title, "пустое название")

with TemporaryDirectory() as directory:
    path = Path(directory) / "selected.json"
    save_json(path, select_tasks(TODOS, 5))
    with open(path, "r", encoding="utf-8") as file:
        restored = json.load(file)
    assert restored == select_tasks(TODOS, 5), restored
    assert ids(restored) == [1, 2, 5]

print("Проверки анализа пройдены")
