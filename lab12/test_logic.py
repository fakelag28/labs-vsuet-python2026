from copy import deepcopy
from logic import add_record, delete_record, find_records, set_completed, statistics, validate_records

records = []
validate_records(records)
assert statistics(records) == {"total": 0, "completed": 0, "remaining": 0, "amount": 0, "categories": {}}
first = add_record(records, "  Python  ", " код ", 4)
second = add_record(records, "Python", "математика", 2)
assert first["title"] == "Python" and first["category"] == "код"
assert first["id"] == 1 and second["id"] == 2
assert len(find_records(records, "PY")) == 2
try:
    find_records(records, "  ")
except ValueError:
    pass
else:
    assert False
assert set_completed(records, 2, True)
assert not set_completed(records, 99, True)
before = deepcopy(records)
assert not delete_record(records, 99)
assert records == before
assert statistics(records) == {"total": 2, "completed": 1, "remaining": 1, "amount": 6, "categories": {"код": 4, "математика": 2}}
assert delete_record(records, 1)
assert add_record(records, "Алгоритмы", "код", 0)["id"] == 3
for record in [{"id": True, "title": "x", "category": "x", "amount": 1, "completed": False}, {"id": 1, "title": "x", "category": "x", "amount": True, "completed": False}, {"id": 1, "title": "x", "category": "x", "amount": 1, "completed": 0}, {"id": 1, "title": " ", "category": "x", "amount": 1, "completed": False}]:
    try:
        validate_records([record])
    except ValueError:
        pass
    else:
        assert False
try:
    validate_records([second, second])
except ValueError:
    pass
else:
    assert False
print("Проверки логики пройдены")
