from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records

records = [{"id": 1, "title": "Python", "category": "учёба", "amount": 4, "completed": False}]
with TemporaryDirectory() as directory:
    path = Path(directory) / "data.json"
    save_records(path, records)
    assert load_records(path) == records
    path.write_text("{", encoding="utf-8")
    try:
        load_records(path)
    except ValueError:
        pass
    else:
        assert False
    assert path.read_text(encoding="utf-8") == "{"
print("Проверки хранения пройдены")
