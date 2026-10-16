source = []
for part in input("Целые числа через пробел: ").split():
    source.append(int(part))

transformed = []
for number in source:
    if number < 0:
        transformed.append(-number)
    else:
        transformed.append(number)

print(f"Исходный список: {source}")
print(f"Новый список: {transformed}")

print(f"Исходный список сохранён: {source}")
