"""Проверки функций из модуля collections_lab (лабораторная работа 8).

Тесты выполняются как обычный скрипт: сравнения записаны через assert,
при успехе печатается строка [OK], иначе возбуждается AssertionError.
Классы и лямбды не используются.
"""

from collections_lab import (
    word_counts,
    common_topics,
    all_topics,
    totals_by_category,
    titles_in_category,
    example_records,
    study_records,
)


def check_equal(name, actual, expected):
    """Сравнивает факт с ожиданием, печатает результат, проверяет assert."""
    assert actual == expected, f"{name}: получено {actual!r}, ожидалось {expected!r}"
    print(f"[OK] {name}: {actual!r}")


def check_true(name, condition):
    """Проверяет истинность условия и печатает результат."""
    assert condition, f"{name}: условие ложно"
    print(f"[OK] {name}")


def test_word_counts():
    """Проверки задания 1: частоты слов."""
    check_equal(
        "word_counts('Python, python! SQL')",
        word_counts("Python, python! SQL"),
        {"python": 2, "sql": 1},
    )
    check_equal("word_counts('!!!')", word_counts("!!!"), {})
    check_equal("word_counts('')", word_counts(""), {})
    check_equal(
        "word_counts('A; a. B,')",
        word_counts("A; a. B,"),
        {"a": 2, "b": 1},
    )


def test_topics():
    """Проверки задания 2: общие и все темы."""
    first = ["python", "sql", "python"]
    second = ["sql", "git"]
    check_equal("common_topics", common_topics(first, second), ["sql"])
    check_equal("all_topics", all_topics(first, second), ["git", "python", "sql"])

    # Один список тем пуст.
    check_equal("common_topics([], ['python'])", common_topics([], ["python"]), [])
    check_equal(
        "all_topics([], ['python', 'sql'])",
        all_topics([], ["python", "sql"]),
        ["python", "sql"],
    )


def test_totals_and_titles():
    """Проверки сводки и поиска по категориям для набора из условия."""
    check_equal(
        "totals_by_category(example_records)",
        totals_by_category(example_records),
        {"основное": 7, "дополнительное": 2},
    )
    check_equal(
        "titles_in_category(example_records, 'основное')",
        titles_in_category(example_records, "основное"),
        ["A", "C"],
    )
    check_equal(
        "titles_in_category(example_records, 'нет')",
        titles_in_category(example_records, "нет"),
        [],
    )
    check_equal("totals_by_category([])", totals_by_category([]), {})


def test_records_unchanged():
    """Проверяет, что функции не меняют входные записи."""
    before = [record.copy() for record in example_records]
    totals_by_category(example_records)
    titles_in_category(example_records, "основное")
    titles_in_category(example_records, "нет")
    check_equal("example_records не изменены", example_records, before)


def test_variant_records():
    """Проверки набора варианта 1: не менее пяти записей, три категории."""
    check_true("study_records: не менее пяти записей", len(study_records) >= 5)
    categories = set()
    for record in study_records:
        categories.add(record["category"])
    check_equal("study_records: три категории", len(categories), 3)
    check_true("study_records: есть повтор категории", len(study_records) > len(categories))
    check_equal(
        "totals_by_category(study_records)",
        totals_by_category(study_records),
        {"лекции": 7, "практика": 8, "лабораторные": 6},
    )


def main():
    """Запускает все проверки."""
    test_word_counts()
    test_topics()
    test_totals_and_titles()
    test_records_unchanged()
    test_variant_records()
    print()
    print("Все проверки пройдены.")


if __name__ == "__main__":
    main()
