"""Итоговый проект. План учебных занятий (работа 12, вариант 1).

Запуск: python main.py
"""

import json
from pathlib import Path

from logic import (
    add_record,
    delete_record,
    find_by_id,
    find_records,
    set_completed,
    statistics,
    validate_records,
)
from storage import load_records, save_records

FOLDER = Path(__file__).resolve().parent
DATA_PATH = FOLDER / "data.json"
UNIT = "ч"

MENU = (
    "\n1 — показать записи\n"
    "2 — добавить запись\n"
    "3 — найти записи\n"
    "4 — изменить статус\n"
    "5 — удалить запись\n"
    "6 — показать статистику\n"
    "7 — сохранить данные\n"
    "8 — выйти\n"
)


def load_at_start():
    """Загрузить данные при запуске.

    Возвращает список записей либо None, если файл повреждён, недоступен или
    имеет неправильную структуру: в этом случае запуск прекращается без
    перезаписи файла.
    """
    try:
        data = load_records(DATA_PATH)
    except FileNotFoundError:
        print(f"Файл {DATA_PATH.name} не найден. Начинаем с пустого списка.")
        return []
    except UnicodeError:
        print(f"Ошибка: файл {DATA_PATH.name} имеет неправильную кодировку, нужна UTF-8.")
        return None
    except json.JSONDecodeError as error:
        # JSONDecodeError — подкласс ValueError, поэтому обработчик идёт раньше.
        print(f"Ошибка: файл {DATA_PATH.name} повреждён: {error}")
        return None
    except OSError as error:
        print(f"Ошибка доступа к файлу {DATA_PATH.name}: {error}")
        return None

    try:
        validate_records(data)
    except ValueError as error:
        print(f"Ошибка структуры данных: {error}")
        return None
    return data


def read_non_empty(prompt):
    """Запросить непустую строку без пробелов по краям."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("Значение не должно быть пустым")


def read_int(prompt):
    """Запросить целое число с повторным вводом при ошибке."""
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Нужно целое число")


def read_amount():
    """Запросить целое количество не меньше нуля."""
    while True:
        amount = read_int("Количество часов: ")
        if amount < 0:
            print("Количество не может быть отрицательным")
            continue
        return amount


def read_yes_no(prompt):
    """Запросить ответ «да» или «нет», повторяя вопрос при другом ответе."""
    while True:
        answer = input(prompt).strip().lower()
        if answer == "да":
            return True
        if answer == "нет":
            return False
        print("Ответьте «да» или «нет»")


def confirm(prompt):
    """Вернуть True только при ответе «да»; другой ответ отменяет действие."""
    return input(prompt).strip().lower() == "да"


def print_record(record):
    """Вывести одну запись одной строкой."""
    status = "выполнено" if record["completed"] else "не выполнено"
    print(
        f"  {record['id']}: {record['title']} | {record['category']} | "
        f"{record['amount']} {UNIT} | {status}"
    )


def record_id_value(record):
    """Вспомогательная функция: идентификатор записи для сортировки."""
    return record["id"]


def show_records(records):
    """Показать все записи по возрастанию идентификатора."""
    if not records:
        print("Нет записей")
        return
    for record in sorted(records, key=record_id_value):
        print_record(record)


def add_dialog(records):
    """Запросить данные новой записи и добавить её."""
    title = read_non_empty("Название занятия: ")
    category = read_non_empty("Категория: ")
    amount = read_amount()
    record = add_record(records, title, category, amount)
    print(f"Добавлена запись с идентификатором {record['id']}")


def find_dialog(records):
    """Найти записи по подстроке названия."""
    while True:
        query = input("Часть названия: ").strip()
        try:
            found = find_records(records, query)
        except ValueError as error:
            print(error)
            continue
        break

    if not found:
        print("Ничего не найдено")
        return
    print(f"Найдено записей: {len(found)}")
    for record in found:
        print_record(record)


def status_dialog(records):
    """Изменить статус записи по её идентификатору."""
    record_id = read_int("Идентификатор записи: ")
    if find_by_id(records, record_id) is None:
        print(f"Запись с идентификатором {record_id} не найдена")
        return
    completed = read_yes_no("Отметить занятие как выполненное? (да/нет): ")
    set_completed(records, record_id, completed)
    print("Статус изменён: " + ("выполнено" if completed else "не выполнено"))


def delete_dialog(records):
    """Удалить запись по идентификатору после подтверждения."""
    record_id = read_int("Идентификатор записи: ")
    if find_by_id(records, record_id) is None:
        print(f"Запись с идентификатором {record_id} не найдена")
        return
    if confirm("Удалить запись? (да/нет): "):
        delete_record(records, record_id)
        print("Запись удалена")
    else:
        print("Удаление отменено")


def statistics_dialog(records):
    """Показать статистику по текущему списку записей."""
    data = statistics(records)
    print(f"Всего записей: {data['total']}")
    print(f"Выполнено: {data['completed']}")
    print(f"Не выполнено: {data['not_completed']}")
    print(f"Сумма запланированных часов: {data['amount_sum']}")
    if not data["by_category"]:
        print("Суммы по категориям: нет данных")
        return
    print("Суммы по категориям:")
    for category in sorted(data["by_category"]):
        print(f"  {category}: {data['by_category'][category]}")


def save_data(records):
    """Сохранить данные. True при успехе, False при ошибке записи."""
    try:
        save_records(DATA_PATH, records)
    except OSError as error:
        print(f"Не удалось сохранить данные: {error}")
        return False
    print(f"Данные сохранены в {DATA_PATH.name}")
    return True


def exit_dialog(records):
    """Предложить сохранить данные. True — выходить, False — остаться в меню."""
    if read_yes_no("Сохранить данные перед выходом? (да/нет): "):
        return save_data(records)
    return True


def main():
    records = load_at_start()
    if records is None:
        print("Работа программы завершена, файл данных не изменён.")
        return

    while True:
        print(MENU)
        command = input("Команда: ").strip()

        if command == "1":
            show_records(records)
        elif command == "2":
            add_dialog(records)
        elif command == "3":
            find_dialog(records)
        elif command == "4":
            status_dialog(records)
        elif command == "5":
            delete_dialog(records)
        elif command == "6":
            statistics_dialog(records)
        elif command == "7":
            save_data(records)
        elif command == "8":
            if exit_dialog(records):
                print("Программа завершена")
                return
        else:
            print("Неизвестная команда, выберите номер от 1 до 8")


if __name__ == "__main__":
    main()
