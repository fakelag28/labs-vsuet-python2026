"""Проверки логики проекта «План учебных занятий» (работа 12).

Запуск: python test_logic.py
"""

from logic import (
    add_record,
    delete_record,
    find_by_id,
    find_records,
    next_id,
    set_completed,
    statistics,
    validate_records,
)

def sample():
    """Вернуть небольшой набор записей для проверок."""
    return [
        {"id": 1, "title": "Математика", "category": "учёба", "amount": 4, "completed": False},
        {"id": 2, "title": "Физика", "category": "учёба", "amount": 2, "completed": True},
        {"id": 3, "title": "Баскетбол", "category": "спорт", "amount": 3, "completed": False},
    ]

def expect_value_error(action, description):
    """Проверить, что действие выбрасывает ValueError."""
    try:
        action()
    except ValueError:
        pass
    else:
        assert False, f"Ошибка не обнаружена: {description}"

def check_empty_query():
    """Пустой поисковый запрос."""
    find_records(sample(), "   ")

def check_root_not_list():
    """Корень данных не список."""
    validate_records({})

def check_record_not_dict():
    """Запись не является объектом."""
    validate_records(["строка"])

def check_missing_completed():
    """В записи отсутствует ключ completed."""
    validate_records([{"id": 1, "title": "A", "category": "B", "amount": 1}])

def check_id_zero():
    """Идентификатор равен нулю."""
    validate_records([{"id": 0, "title": "A", "category": "B", "amount": 1, "completed": True}])

def check_id_is_bool():
    """Идентификатор передан логическим значением."""
    validate_records([{"id": True, "title": "A", "category": "B", "amount": 1, "completed": True}])

def check_empty_title():
    """Название состоит из пробелов."""
    validate_records([{"id": 1, "title": "  ", "category": "B", "amount": 1, "completed": True}])

def check_empty_category():
    """Категория пустая."""
    validate_records([{"id": 1, "title": "A", "category": "", "amount": 1, "completed": True}])

def check_negative_amount():
    """Количество отрицательное."""
    validate_records([{"id": 1, "title": "A", "category": "B", "amount": -1, "completed": True}])

def check_amount_is_string():
    """Количество передано строкой."""
    validate_records([{"id": 1, "title": "A", "category": "B", "amount": "abc", "completed": True}])

def check_amount_is_bool():
    """Количество передано логическим значением."""
    validate_records([{"id": 1, "title": "A", "category": "B", "amount": True, "completed": True}])

def check_completed_is_number():
    """Поле completed передано числом."""
    validate_records([{"id": 1, "title": "A", "category": "B", "amount": 1, "completed": 1}])

def check_duplicate_id():
    """Идентификатор записи повторяется."""
    validate_records([
        {"id": 1, "title": "A", "category": "B", "amount": 1, "completed": True},
        {"id": 1, "title": "C", "category": "B", "amount": 1, "completed": False},
    ])

data = statistics(sample())
assert data["total"] == 3, data
assert data["completed"] == 1, data
assert data["not_completed"] == 2, data
assert data["amount_sum"] == 9, data
assert data["by_category"] == {"учёба": 6, "спорт": 3}, data
assert statistics([]) == {
    "total": 0,
    "completed": 0,
    "not_completed": 0,
    "amount_sum": 0,
    "by_category": {},
}

records = sample()
before = [record.copy() for record in records]
statistics(records)
assert records == before, "Статистика изменила записи"

records = sample()
added = add_record(records, "  Химия  ", "  учёба ", 5)
assert added["id"] == 4, added
assert added["title"] == "Химия", added
assert added["category"] == "учёба", added
assert added["amount"] == 5, added
assert added["completed"] is False, added
assert len(records) == 4

second = add_record(records, "Химия", "учёба", 1)
assert second["id"] == 5, second

assert add_record([], "Первая", "учёба", 2)["id"] == 1
assert next_id([]) == 1
assert next_id(sample()) == 4

records = sample()
assert delete_record(records, 1) is True
assert [record["id"] for record in records] == [2, 3]
assert add_record(records, "Новая", "учёба", 1)["id"] == 4

records = sample()
assert [record["id"] for record in find_records(records, "мат")] == [1]
assert [record["id"] for record in find_records(records, "МАТ")] == [1]
assert len(find_records(records, "физ")) == 1
assert find_records(records, "нет такого") == []
expect_value_error(check_empty_query, "пустой поисковый запрос")

before = [record.copy() for record in records]
find_records(records, "а")
assert records == before, "Поиск изменил записи"

records = sample()
assert set_completed(records, 1, True) is True
assert records[0]["completed"] is True
assert set_completed(records, 1, False) is True
assert records[0]["completed"] is False
assert set_completed(records, 99, True) is False
assert len(records) == 3
assert records[0] == {"id": 1, "title": "Математика", "category": "учёба", "amount": 4, "completed": False}

records = sample()
assert delete_record(records, 2) is True
assert [record["id"] for record in records] == [1, 3]
assert delete_record(records, 99) is False
assert len(records) == 2
assert find_by_id(records, 1) == records[0]
assert find_by_id(records, 99) is None

assert validate_records(sample()) == sample()
assert validate_records([]) == []
extra = [{"id": 1, "title": "A", "category": "B", "amount": 0, "completed": True, "note": "тест"}]
assert validate_records(extra) == extra

expect_value_error(check_root_not_list, "корень не список")
expect_value_error(check_record_not_dict, "запись не объект")
expect_value_error(check_missing_completed, "отсутствует ключ completed")
expect_value_error(check_id_zero, "id равен нулю")
expect_value_error(check_id_is_bool, "id = True")
expect_value_error(check_empty_title, "пустое название")
expect_value_error(check_empty_category, "пустая категория")
expect_value_error(check_negative_amount, "amount = -1")
expect_value_error(check_amount_is_string, "amount строкой")
expect_value_error(check_amount_is_bool, "amount = True")
expect_value_error(check_completed_is_number, "completed = 1")
expect_value_error(check_duplicate_id, "повторный id")

print("Проверки логики пройдены")
