from pathlib import Path
from logic import add_record, delete_record, find_records, set_completed, statistics
from storage import load_records, save_records


def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Значение не должно быть пустым")


def read_integer(prompt, minimum):
    while True:
        try:
            value = int(input(prompt))
            if value >= minimum:
                return value
        except ValueError:
            pass
        print(f"Введите целое число не меньше {minimum}")


def show_records(records):
    if not records:
        print("Нет записей")
    for record in sorted(records, key=lambda item: item["id"]):
        status = "выполнено" if record["completed"] else "не выполнено"
        print(f"{record['id']}: {record['title']} | {record['category']} | {record['amount']} ч. | {status}")


def save(path, records):
    try:
        save_records(path, records)
        print("Данные сохранены")
        return True
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Ошибка сохранения: {error}")
        return False


def main():
    path = Path(__file__).resolve().parent / "data.json"
    try:
        records = load_records(path)
    except FileNotFoundError:
        print("Файл данных отсутствует, создан пустой список")
        records = []
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Ошибка загрузки: {error}")
        return
    while True:
        print("\n1. Показать  2. Добавить  3. Найти  4. Статус  5. Удалить  6. Статистика  7. Сохранить  8. Выход")
        choice = input("Команда: ").strip()
        if choice == "1":
            show_records(records)
        elif choice == "2":
            title = read_text("Название: ")
            category = read_text("Категория: ")
            amount = read_integer("Часы: ", 0)
            print(f"Добавлена запись {add_record(records, title, category, amount)['id']}")
        elif choice == "3":
            found = find_records(records, read_text("Поиск: "))
            if found:
                show_records(found)
            else:
                print("Ничего не найдено")
        elif choice == "4":
            identifier = read_integer("ID: ", 1)
            if not any(record["id"] == identifier for record in records):
                print("Запись не найдена")
                continue
            while True:
                status = input("Статус (1 — выполнено, 0 — не выполнено): ").strip()
                if status in ("0", "1"):
                    break
                print("Введите 0 или 1")
            set_completed(records, identifier, status == "1")
            print("Статус изменён")
        elif choice == "5":
            identifier = read_integer("ID: ", 1)
            if not any(record["id"] == identifier for record in records):
                print("Запись не найдена")
            elif input("Удалить запись? Введите да: ").strip().lower() == "да":
                delete_record(records, identifier)
                print("Запись удалена")
            else:
                print("Удаление отменено")
        elif choice == "6":
            result = statistics(records)
            print(f"Всего: {result['total']}, выполнено: {result['completed']}, не выполнено: {result['remaining']}, часов: {result['amount']}")
            for category, amount in result["categories"].items():
                print(f"{category}: {amount} ч.")
        elif choice == "7":
            save(path, records)
        elif choice == "8":
            while True:
                answer = input("Сохранить данные перед выходом (да/нет)? ").strip().lower()
                if answer == "нет":
                    return
                if answer == "да":
                    if save(path, records):
                        return
                    break
                print("Введите да или нет")
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
