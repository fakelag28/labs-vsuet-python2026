import json
from pathlib import Path
from analysis import completion_counts, leader_tasks, select_tasks, top_users, validate_todos


def main():
    directory = Path(__file__).resolve().parent
    try:
        with open(directory / "todos.json", encoding="utf-8") as file:
            todos = json.load(file)
        validate_todos(todos)
        while True:
            try:
                user_id = int(input("Положительный ID пользователя: "))
                if user_id > 0:
                    break
            except ValueError:
                pass
            print("Введите положительное целое число")
        counts = completion_counts(todos)
        leaders = top_users(counts)
        print(f"Количество завершённых задач: {counts}")
        print(f"Лидеры: {leaders}")
        for name, data in (("leaders.json", leader_tasks(todos, leaders)), ("selected.json", select_tasks(todos, user_id))):
            with open(directory / name, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
        print("Результаты сохранены")
    except FileNotFoundError:
        print("Файл не найден")
    except UnicodeError as error:
        print(f"Ошибка кодировки: {error}")
    except json.JSONDecodeError as error:
        print(f"Ошибка JSON: {error}")
    except ValueError as error:
        print(f"Ошибка данных: {error}")
    except OSError as error:
        print(f"Ошибка доступа: {error}")


if __name__ == "__main__":
    main()
