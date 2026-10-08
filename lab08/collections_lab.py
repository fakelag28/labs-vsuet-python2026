"""Лабораторная работа 8. Словари, множества и кортежи.

Модуль собирает функции для трёх обязательных заданий и варианта 1:
подсчёт частот слов, работу с учебными интересами через множества,
обработку записи-словаря и список словарей-записей по категориям.

Все ключи словарей — строки. Списки и словари-записи, переданные
в функции, не изменяются: функции только читают их.
"""

# Знаки, которые удаляются с краёв слова (задание 1).
PUNCTUATION = ".,!?;:"

# Набор записей из условия лабораторной работы (для общей проверки).
example_records = [
    {"title": "A", "category": "основное", "amount": 4},
    {"title": "B", "category": "дополнительное", "amount": 2},
    {"title": "C", "category": "основное", "amount": 3},
]

# Вариант 1, предметная область «Учебные занятия», amount — «Часы».
# Не менее пяти содержательных записей с тремя категориями,
# категория «лекции» повторяется.
study_records = [
    {"title": "Математика", "category": "лекции", "amount": 4},
    {"title": "Физика", "category": "лекции", "amount": 3},
    {"title": "Программирование", "category": "практика", "amount": 5},
    {"title": "Базы данных", "category": "лабораторные", "amount": 2},
    {"title": "Математика", "category": "практика", "amount": 3},
    {"title": "Физика", "category": "лабораторные", "amount": 4},
]


def word_counts(text):
    """Возвращает словарь «слово → количество» для текста.

    Слово приводится к нижнему регистру, у каждого слова удаляются
    знаки .,!?;: с краёв, пустые результаты пропускаются.
    Пустой текст даёт пустой словарь.
    """
    counts = {}
    for raw_word in text.split():
        word = raw_word.lower().strip(PUNCTUATION)
        if word == "":
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def print_word_counts(counts):
    """Выводит пары «слово: количество» в алфавитном порядке ключей."""
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    """Возвращает отсортированный список общих тем двух списков.

    Темы уже приведены к нижнему регистру, сравнение точное.
    Используется пересечение множеств.
    """
    return sorted(set(first) & set(second))


def all_topics(first, second):
    """Возвращает отсортированный список всех уникальных тем.

    Используется объединение множеств.
    """
    return sorted(set(first) | set(second))


def totals_by_category(records):
    """Возвращает словарь сумм amount по категориям.

    Ключ — категория, значение — сумма amount всех её записей.
    Пустой список даёт пустой словарь.
    """
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    """Возвращает названия записей категории в исходном порядке.

    Если записей с такой категорией нет, возвращается пустой список.
    """
    titles = []
    for record in records:
        if record["category"] == category:
            titles.append(record["title"])
    return titles


def print_category_totals(records):
    """Выводит суммы amount по категориям в алфавитном порядке."""
    totals = totals_by_category(records)
    for category in sorted(totals):
        print(f"{category}: {totals[category]}")


if __name__ == "__main__":
    print("=== Задание 1. Частоты слов ===")
    print_word_counts(word_counts("Python, python! SQL"))

    print()
    print("=== Задание 2. Учебные интересы ===")
    first_topics = ["python", "sql", "python"]
    second_topics = ["sql", "git"]
    print(f"Общие темы: {common_topics(first_topics, second_topics)}")
    print(f"Все темы: {all_topics(first_topics, second_topics)}")

    print()
    print("=== Задание 3. Запись и пара ===")
    lesson = {"title": "Python", "hours": 4}
    lesson["hours"] = 6
    lesson["completed"] = False
    pair = (lesson["title"], lesson["hours"])
    title, hours = pair
    print(f"Запись: {lesson}")
    print(f"Кортеж: {pair}")
    print(f"Название: {title}, часы: {hours}")

    print()
    print("=== Пример из условия ===")
    print_category_totals(example_records)

    print()
    print("=== Вариант 1. Учебные занятия ===")
    print("Сводка по категориям:")
    print_category_totals(study_records)

    print()
    print("Введите категорию для поиска:")
    category = input().strip()
    print(f"Пример из условия, категория {category!r}: "
          f"{titles_in_category(example_records, category)}")
    print(f"Учебные занятия, категория {category!r}: "
          f"{titles_in_category(study_records, category)}")
