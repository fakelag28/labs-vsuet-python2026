"""Лабораторная работа 11. Анализ набора задач и сохранение результатов.

Индивидуальный вариант 1: для выбранного пользователя отбираются все задачи.
"""

import json
from pathlib import Path

from analysis import completion_counts, select_tasks, top_users, validate_todos

FOLDER = Path(__file__).resolve().parent
TODOS_PATH = FOLDER / "todos.json"
LEADERS_PATH = FOLDER / "leaders.json"
SELECTED_PATH = FOLDER / "selected.json"

def read_todos(path):
    """Прочитать набор задач из файла и проверить структуру.

    Ошибки не обрабатываются здесь: их разбирает main(), чтобы показать
    понятное сообщение.
    """
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return validate_todos(data)

def save_json(path, data):
    """Записать данные в JSON в UTF-8."""
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def read_user_id():
    """Запросить положительный целый идентификатор пользователя."""
    while True:
        text = input("Идентификатор пользователя: ").strip()
        try:
            user_id = int(text)
        except ValueError:
            print("Нужно целое число")
            continue
        if user_id <= 0:
            print("Число должно быть больше нуля")
            continue
        return user_id

def leaders_tasks(todos, leaders):
    """Вернуть выполненные задачи лидеров в исходном порядке."""
    return [
        record
        for record in todos
        if record["completed"] and record["userId"] in leaders
    ]

def main():
    try:
        todos = read_todos(TODOS_PATH)
    except FileNotFoundError:
        print(f"Файл не найден: {TODOS_PATH.name}")
        return
    except UnicodeError:
        print("Файл имеет неправильную кодировку, ожидается UTF-8")
        return
    except json.JSONDecodeError as error:
        print(f"Ошибка разбора JSON: {error}")
        return
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return
    except OSError as error:
        print(f"Ошибка доступа к файлу: {error}")
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)

    print(f"Всего записей: {len(todos)}")
    print("Выполнено задач по пользователям:")
    for user_id in sorted(counts):
        print(f"  пользователь {user_id}: {counts[user_id]}")
    if leaders:
        print("Лидеры: " + ", ".join(str(user_id) for user_id in leaders))
    else:
        print("Лидеров нет: ни одна задача не выполнена")

    user_id = read_user_id()
    selected = select_tasks(todos, user_id)
    print(f"Задач пользователя {user_id}: {len(selected)}")
    for record in selected:
        print(f"  {record['id']}: {record['title']}")

    try:
        save_json(LEADERS_PATH, leaders_tasks(todos, leaders))
        save_json(SELECTED_PATH, selected)
    except OSError as error:
        print(f"Не удалось сохранить результаты: {error}")
        return
    print(f"Сохранено: {LEADERS_PATH.name}, {SELECTED_PATH.name}")

if __name__ == "__main__":
    main()
