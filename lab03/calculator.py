# calculator.py
# Лабораторная работа 3, задание 2: калькулятор с одной операцией.
# Ввод: первое число, второе число, операция.

first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ")

if operation == "+":
    result = first + second
    print(f"Результат: {result:.2f}")
elif operation == "-":
    result = first - second
    print(f"Результат: {result:.2f}")
elif operation == "*":
    result = first * second
    print(f"Результат: {result:.2f}")
elif operation == "/":
    if second == 0:
        print("Деление на ноль запрещено")
    else:
        result = first / second
        print(f"Результат: {result:.2f}")
else:
    print("Неизвестная операция")
