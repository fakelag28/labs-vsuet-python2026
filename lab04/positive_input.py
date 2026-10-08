rejected = 0
number = int(input("Введите положительное целое число: "))

while number <= 0:
    rejected += 1
    number = int(input("Число должно быть положительным, попробуйте снова: "))

print(f"Квадрат: {number * number}")
print(f"Отклонено попыток: {rejected}")
