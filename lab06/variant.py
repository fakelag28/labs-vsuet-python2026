numbers = []
for part in input("Целые числа через пробел: ").split():
    numbers.append(int(part))

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

print(f"Чётные числа: {evens}")
print(f"Количество: {len(evens)}")
print(f"Сумма: {sum(evens)}")
print(f"Отсортированная копия: {sorted(evens)}")
