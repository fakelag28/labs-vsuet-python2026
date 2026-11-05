from functions import average, normalize_text, select_numbers, sum_digits


def main():
    number = int(input("Целое число: "))
    numbers = [int(part) for part in input("Числа через пробел: ").split()]
    text = input("Текст: ")
    threshold = int(input("Неотрицательный порог: "))
    while threshold < 0:
        threshold = int(input("Порог должен быть неотрицательным: "))
    print(f"Сумма цифр: {sum_digits(number)}")
    result = average(numbers)
    print(f"Среднее: {result if result is not None else 'Нет данных'}")
    print(f"Текст: {normalize_text(text)}")
    print(f"Выборка: {select_numbers(numbers, threshold)}")


if __name__ == "__main__":
    main()
