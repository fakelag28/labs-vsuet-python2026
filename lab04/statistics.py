n = int(input("Сколько чисел будет введено (n >= 1): "))

total = 0
positive = 0

for index in range(n):
    number = int(input(f"Число {index + 1}: "))
    total += number
    if number > 0:
        positive += 1
    if index == 0:
        maximum = number
    elif number > maximum:
        maximum = number

print(f"Сумма: {total}")
print(f"Положительных: {positive}")
print(f"Максимум: {maximum}")
