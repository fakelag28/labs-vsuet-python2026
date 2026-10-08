# Лабораторная работа 6. Задание 1. Статистика
# Ввод целых чисел одной строкой; вывод количества, суммы,
# минимума, максимума и среднего с двумя знаками после точки.

numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

if not numbers:
    # Пустой ввод: min()/max() вызывать нельзя, делить на ноль тоже.
    print("Нет данных")
else:
    print(f"Количество: {len(numbers)}")
    print(f"Сумма: {sum(numbers)}")
    print(f"Минимум: {min(numbers)}")
    print(f"Максимум: {max(numbers)}")
    print(f"Среднее: {sum(numbers) / len(numbers):.2f}")
