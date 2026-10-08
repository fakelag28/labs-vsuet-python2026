# Лабораторная работа 6. Задание 2. Независимое преобразование
# Новый список: отрицательные числа заменены их модулями.
# Исходный список должен сохраниться. Пустой ввод допустим.

source = []
for part in input("Целые числа через пробел: ").split():
    source.append(int(part))

# Строим новый список отдельно, не изменяя исходный.
# Эквивалент списковым включением:
#   transformed = [abs(number) for number in source]
transformed = []
for number in source:
    if number < 0:
        transformed.append(-number)
    else:
        transformed.append(number)

print(f"Исходный список: {source}")
print(f"Новый список: {transformed}")

# Демонстрация того, что исходный список не изменился.
print(f"Исходный список сохранён: {source}")
