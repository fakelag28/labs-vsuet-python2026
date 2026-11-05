import json
from logic import validate_records


def load_records(path):
    with open(path, encoding="utf-8") as file:
        records = json.load(file)
    validate_records(records)
    return records


def save_records(path, records):
    validate_records(records)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
        file.write("\n")
