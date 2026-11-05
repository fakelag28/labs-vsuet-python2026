def sum_digits(number):
    number = abs(number)
    total = 0
    while number:
        total += number % 10
        number //= 10
    return total


def average(numbers):
    return sum(numbers) / len(numbers) if numbers else None


def normalize_text(text):
    return " ".join(text.lower().split())


def select_numbers(numbers, threshold):
    return [number for number in numbers if number > threshold]
