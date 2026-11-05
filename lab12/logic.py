def validate_records(records):
    if not isinstance(records, list):
        raise ValueError("Ожидается список записей")
    identifiers = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Запись должна быть объектом")
        identifier = record.get("id")
        if type(identifier) is not int or identifier <= 0 or identifier in identifiers:
            raise ValueError("ID должен быть уникальным положительным целым")
        identifiers.add(identifier)
        for key in ("title", "category"):
            if not isinstance(record.get(key), str) or not record[key].strip():
                raise ValueError(f"Поле {key} должно быть непустой строкой")
        if type(record.get("amount")) is not int or record["amount"] < 0:
            raise ValueError("Количество часов должно быть неотрицательным целым")
        if type(record.get("completed")) is not bool:
            raise ValueError("Статус должен быть логическим значением")


def add_record(records, title, category, amount):
    if not isinstance(title, str) or not isinstance(category, str):
        raise ValueError("Название и категория должны быть строками")
    record = {"id": max((item["id"] for item in records), default=0) + 1, "title": title.strip(), "category": category.strip(), "amount": amount, "completed": False}
    validate_records([record])
    records.append(record)
    return record


def find_records(records, query):
    query = query.strip().casefold()
    if not query:
        raise ValueError("Поисковый запрос не должен быть пустым")
    return [record for record in records if query in record["title"].casefold()]


def set_completed(records, record_id, completed):
    if type(completed) is not bool:
        raise ValueError("Статус должен быть логическим значением")
    for record in records:
        if record["id"] == record_id:
            record["completed"] = completed
            return True
    return False


def delete_record(records, record_id):
    for index, record in enumerate(records):
        if record["id"] == record_id:
            del records[index]
            return True
    return False


def statistics(records):
    completed = sum(record["completed"] for record in records)
    categories = {}
    for record in records:
        category = record["category"].strip()
        categories[category] = categories.get(category, 0) + record["amount"]
    return {"total": len(records), "completed": completed, "remaining": len(records) - completed, "amount": sum(record["amount"] for record in records), "categories": dict(sorted(categories.items()))}
