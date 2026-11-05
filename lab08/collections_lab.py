def word_counts(text):
    counts = {}
    for part in text.lower().split():
        word = part.strip(".,!?;:")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def print_counts(counts):
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")


def common_topics(first, second):
    return sorted(set(first) & set(second))


def all_topics(first, second):
    return sorted(set(first) | set(second))


def totals_by_category(records):
    totals = {}
    for record in records:
        category = record["category"]
        totals[category] = totals.get(category, 0) + record["amount"]
    return totals


def titles_in_category(records, category):
    return [record["title"] for record in records if record["category"] == category]


def main():
    print_counts(word_counts(input("Текст: ")))
    first = input("Темы первого студента: ").lower().split()
    second = input("Темы второго студента: ").lower().split()
    print(f"Общие темы: {common_topics(first, second)}")
    print(f"Все темы: {all_topics(first, second)}")
    lesson = {"title": "Python", "hours": 4}
    lesson["hours"] = 6
    lesson["completed"] = False
    title, hours = (lesson["title"], lesson["hours"])
    print(f"Занятие: {title}, часов: {hours}")
    records = [
        {"title": "Python", "category": "программирование", "amount": 4},
        {"title": "Алгоритмы", "category": "программирование", "amount": 3},
        {"title": "Алгебра", "category": "математика", "amount": 2},
        {"title": "Геометрия", "category": "математика", "amount": 2},
        {"title": "Английский", "category": "языки", "amount": 3},
    ]
    print_counts(totals_by_category(records))
    print(titles_in_category(records, input("Категория: ")))


if __name__ == "__main__":
    main()
