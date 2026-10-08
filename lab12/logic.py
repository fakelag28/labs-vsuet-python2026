"""Логика итогового проекта «План учебных занятий» (работа 12, вариант 1).

Запись — словарь
{"id": 1, "title": "Математический анализ", "category": "учёба", "amount": 4,
 "completed": true},
где amount — запланированные часы, completed — занятие завершено.

Контракты функций:
* validate_records(records) — только проверяет данные, возвращает тот же
  список, при нарушении выбрасывает ValueError;
* add_record(records, title, category, amount) — изменяет список, возвращает
  добавленную запись; идентификатор на единицу больше максимального;
* find_records(records, query) — возвращает новый список, исходный не
  изменяет; пустой запрос отклоняется через ValueError;
* set_completed(records, record_id, completed) — изменяет список, возвращает
  True при успехе и False, если запись не найдена;
* delete_record(records, record_id) — изменяет список, возвращает True при
  успехе и False, если запись не найдена;
* statistics(records) — возвращает новый словарь, исходный список не изменяет.
"""

KEYS = ("id", "title", "category", "amount", "completed")

def validate_records(records):
    """Проверить весь набор записей и вернуть его без изменений."""
    if not isinstance(records, list):
        raise ValueError("Корень JSON должен быть списком записей")

    seen_ids = set()
    for number, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Запись {number}: ожидался объект")

        for key in KEYS:
            if key not in record:
                raise ValueError(f"Запись {number}: отсутствует ключ {key}")

        if type(record["id"]) is not int:
            raise ValueError(f"Запись {number}: id должен быть целым числом")
        if record["id"] <= 0:
            raise ValueError(f"Запись {number}: id должен быть больше нуля")
        if record["id"] in seen_ids:
            raise ValueError(f"Запись {number}: id {record['id']} повторяется")
        seen_ids.add(record["id"])

        if not isinstance(record["title"], str) or not record["title"].strip():
            raise ValueError(f"Запись {number}: название должно быть непустой строкой")

        if not isinstance(record["category"], str) or not record["category"].strip():
            raise ValueError(f"Запись {number}: категория должна быть непустой строкой")

        if type(record["amount"]) is not int:
            raise ValueError(f"Запись {number}: количество должно быть целым числом")
        if record["amount"] < 0:
            raise ValueError(f"Запись {number}: количество не может быть отрицательным")

        if type(record["completed"]) is not bool:
            raise ValueError(f"Запись {number}: completed должен быть True или False")

    return records

def next_id(records):
    """Идентификатор новой записи: максимум существующих плюс 1."""
    if not records:
        return 1
    return max(record["id"] for record in records) + 1

def add_record(records, title, category, amount):
    """Добавить запись с начальным статусом False и вернуть её.

    Название и категория записываются без пробелов по краям. Аргументы
    проверяет вызывающая сторона.
    """
    record = {
        "id": next_id(records),
        "title": title.strip(),
        "category": category.strip(),
        "amount": amount,
        "completed": False,
    }
    records.append(record)
    return record

def find_by_id(records, record_id):
    """Вернуть запись по идентификатору или None."""
    for record in records:
        if record["id"] == record_id:
            return record
    return None

def find_records(records, query):
    """Найти записи по непустой подстроке названия без учёта регистра."""
    part = query.strip().lower()
    if not part:
        raise ValueError("Поисковый запрос не должен быть пустым")
    return [record for record in records if part in record["title"].lower()]

def set_completed(records, record_id, completed):
    """Установить выбранный статус записи. False, если запись не найдена."""
    record = find_by_id(records, record_id)
    if record is None:
        return False
    record["completed"] = completed
    return True

def delete_record(records, record_id):
    """Удалить запись по идентификатору. False, если запись не найдена."""
    for index, record in enumerate(records):
        if record["id"] == record_id:
            records.pop(index)
            return True
    return False

def statistics(records):
    """Вернуть статистику по текущему списку записей.

    Категории сравниваются точно после удаления краевых пробелов.
    """
    completed = 0
    amount_sum = 0
    by_category = {}
    for record in records:
        if record["completed"]:
            completed += 1
        amount_sum += record["amount"]
        category = record["category"].strip()
        by_category[category] = by_category.get(category, 0) + record["amount"]

    return {
        "total": len(records),
        "completed": completed,
        "not_completed": len(records) - completed,
        "amount_sum": amount_sum,
        "by_category": by_category,
    }
