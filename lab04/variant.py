n = int(input("Сколько чисел будет введено (n >= 0): "))

count = 0
total = 0

for index in range(n):
    number = int(input(f"Число {index + 1}: "))
    if number % 2 == 0:
        count += 1
        total += number

print(f"Количество чётных: {count}")
print(f"Сумма чётных: {total}")
