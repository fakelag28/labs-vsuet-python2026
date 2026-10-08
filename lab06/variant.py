# Лабораторная работа 6. Индивидуальный вариант 1. "Чётные числа"
# Ввод целых чисел одной строкой -> список чётных значений.
# Вывод: список в исходном порядке, количество, сумма,
# новая отсортированная по возрастанию копия.

numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

# Список чётных значений (повторы сохраняются).
# Эквивалент списковым включением:
#   evens = [number for number in numbers if number % 2 == 0]
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(f"Чётные числа: {evens}")
print(f"Количество: {len(evens)}")
print(f"Сумма: {sum(evens)}")
print(f"Отсортированная копия: {sorted(evens)}")
