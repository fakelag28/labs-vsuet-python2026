import json
from pathlib import Path
from tempfile import TemporaryDirectory
from analysis import completion_counts, leader_tasks, select_tasks, top_users, validate_todos

with open(Path(__file__).resolve().parent / "todos.json", encoding="utf-8") as file:
    todos = json.load(file)
validate_todos(todos)
counts = completion_counts(todos)
assert counts == {5: 2, 10: 2}
assert top_users(counts) == [5, 10]
selected = leader_tasks(todos, top_users(counts))
assert [item["id"] for item in selected] == [1, 3, 4, 5]
assert [item["id"] for item in select_tasks(todos, 5)] == [1, 2, 5]
assert select_tasks(todos, 99) == []
assert top_users(completion_counts([])) == []
assert top_users(completion_counts([todos[1]])) == []
assert leader_tasks([todos[1]], []) == []
assert top_users({1: 2, 2: 1}) == [1]
assert top_users({1: 2, 2: 2}) == [1, 2]
invalid = [{}, [todos[0], todos[0]], [{"id": 1, "title": "x", "completed": False}], [{"id": 1, "userId": 1, "title": "x", "completed": "false"}], [{"id": True, "userId": 1, "title": "x", "completed": False}]]
for data in invalid:
    try:
        validate_todos(data)
    except ValueError:
        pass
    else:
        assert False, "Ошибка не обнаружена"
with TemporaryDirectory() as directory:
    path = Path(directory) / "result.json"
    path.write_text(json.dumps(selected, ensure_ascii=False), encoding="utf-8")
    assert json.loads(path.read_text(encoding="utf-8")) == selected
print("Проверки пройдены")
