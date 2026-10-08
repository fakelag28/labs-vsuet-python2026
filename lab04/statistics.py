# Лабораторная работа 4. Задание 2. Статистика потока
# Ввод n >= 1, затем ровно n целых чисел.
# Вывод: сумма, число положительных значений и максимум.
# Список не используется, подсчёт ведётся в цикле.

n = int(input("Сколько чисел будет введено (n >= 1): "))

total = 0
positive = 0

for index in range(n):
    number = int(input(f"Число {index + 1}: "))
    total += number
    if number > 0:
        positive += 1
    if index == 0:
        # Максимум инициализируем первым введённым значением,
        # иначе для всех отрицательных чисел ответ был бы неверным.
        maximum = number
    elif number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Положительных: {positive}")
print(f"Максимум: {maximum}")
