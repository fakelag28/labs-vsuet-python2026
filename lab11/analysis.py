def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError("Ожидается список задач")
    identifiers = set()
    for record in data:
        if not isinstance(record, dict):
            raise ValueError("Задача должна быть объектом")
        for key in ("id", "userId"):
            if type(record.get(key)) is not int or record[key] <= 0:
                raise ValueError(f"{key} должен быть положительным целым")
        if record["id"] in identifiers:
            raise ValueError("Повторный id")
        identifiers.add(record["id"])
        if not isinstance(record.get("title"), str) or not record["title"].strip():
            raise ValueError("Название должно быть непустой строкой")
        if type(record.get("completed")) is not bool:
            raise ValueError("completed должен быть логическим значением")


def completion_counts(todos):
    counts = {}
    for todo in todos:
        user = todo["userId"]
        counts[user] = counts.get(user, 0) + int(todo["completed"])
    return counts


def top_users(counts):
    if not counts or max(counts.values()) == 0:
        return []
    maximum = max(counts.values())
    return sorted(user for user, count in counts.items() if count == maximum)


def select_tasks(todos, user_id, parameter=None):
    return [todo for todo in todos if todo["userId"] == user_id]


def leader_tasks(todos, leaders):
    return [todo for todo in todos if todo["completed"] and todo["userId"] in leaders]
