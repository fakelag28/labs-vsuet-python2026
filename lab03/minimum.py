# minimum.py
# Лабораторная работа 3, задание 1: минимум трёх чисел.
# Функции min, max и сортировка не используются — только ветвление.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a <= b and a <= c:
    minimum = a
elif b <= a and b <= c:
    minimum = b
else:
    minimum = c

print("Минимум:", minimum)
