"""Проверка и анализ набора задач (лабораторная работа 11).

Запись набора — словарь вида
{"id": 1, "userId": 5, "title": "Ввод", "completed": true}.

Все функции получают готовый список записей и не изменяют его.

Индивидуальный вариант 1: для выбранного пользователя отбираются все его
задачи, дополнительный параметр не используется.
"""


def validate_todos(data):
    """Проверить набор задач и вернуть его без изменений.

    Корень — список, каждая запись — словарь с положительными целыми id и
    userId, непустой строкой title и логическим completed. Идентификатор id
    уникален. Дополнительные ключи допустимы.
    При нарушении структуры выбрасывает ValueError с пояснением.
    """
    if not isinstance(data, list):
        raise ValueError("Корень JSON должен быть списком записей")

    seen_ids = set()
    for number, record in enumerate(data, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Запись {number}: ожидался объект")

        for key in ("id", "userId", "title", "completed"):
            if key not in record:
                raise ValueError(f"Запись {number}: отсутствует ключ {key}")

        # type(...) is int отсекает логические значения, которые тоже
        # проходят проверку isinstance(value, int).
        if type(record["id"]) is not int:
            raise ValueError(f"Запись {number}: id должен быть целым числом")
        if record["id"] <= 0:
            raise ValueError(f"Запись {number}: id должен быть больше нуля")
        if record["id"] in seen_ids:
            raise ValueError(f"Запись {number}: id {record['id']} повторяется")
        seen_ids.add(record["id"])

        if type(record["userId"]) is not int:
            raise ValueError(f"Запись {number}: userId должен быть целым числом")
        if record["userId"] <= 0:
            raise ValueError(f"Запись {number}: userId должен быть больше нуля")

        if not isinstance(record["title"], str) or not record["title"].strip():
            raise ValueError(f"Запись {number}: title должен быть непустой строкой")

        if type(record["completed"]) is not bool:
            raise ValueError(f"Запись {number}: completed должен быть True или False")

    return data


def completion_counts(todos):
    """Вернуть словарь «идентификатор пользователя → выполненных задач».

    В словарь попадают все пользователи набора, в том числе те, у которых
    нет выполненных задач. Исходный список не изменяется.
    """
    counts = {}
    for record in todos:
        user_id = record["userId"]
        if user_id not in counts:
            counts[user_id] = 0
        if record["completed"]:
            counts[user_id] += 1
    return counts


def top_users(counts):
    """Вернуть отсортированный список лидеров по числу выполненных задач.

    Для пустого словаря или максимального значения 0 возвращает пустой список.
    """
    if not counts:
        return []
    best = max(counts.values())
    if best == 0:
        return []
    return sorted(user_id for user_id in counts if counts[user_id] == best)


def select_tasks(todos, user_id, parameter=None):
    """Вернуть новый список задач пользователя user_id.

    Вариант 1 отбирает все задачи пользователя, поэтому parameter не нужен
    и остаётся равным None. Порядок записей сохраняется.
    Для неизвестного пользователя результат — пустой список.
    """
    return [record for record in todos if record["userId"] == user_id]
