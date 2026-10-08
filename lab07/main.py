"""Точка входа: демонстрация функций из модуля functions.

Взаимодействие с пользователем вынесено сюда, а вычисления живут в
functions.py. Все результаты показываются через print().
"""

from functions import average, normalize_text, select_numbers, sum_digits

def read_numbers_line():
    """Запросить строку чисел через пробел и вернуть список целых.

    Пустая строка даёт пустой список, что позволяет показать ветку
    «Нет данных» для среднего.
    """
    line = input("Введите числа через пробел: ")
    return [int(part) for part in line.split()]

def main():
    """Запросить данные и продемонстрировать все четыре функции."""
    number = int(input("Введите целое число: "))
    print("Сумма цифр модуля числа:", sum_digits(number))

    numbers = read_numbers_line()
    mean = average(numbers)
    if mean is None:
        print("Среднее:", "Нет данных")
    else:
        print("Среднее:", mean)

    text = input("Введите произвольный текст: ")
    print("Нормализованный текст:", normalize_text(text))

    threshold = int(input("Введите порог: "))
    selected = select_numbers(numbers, threshold)
    print("Числа больше порога:", selected)

if __name__ == "__main__":
    main()
