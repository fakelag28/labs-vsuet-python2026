"""Автоматические проверки функций из модуля functions.

Базовый набор из условия работы плюс проверки индивидуального варианта 1.
Запуск: python test_functions.py
"""

from functions import average, normalize_text, select_numbers, sum_digits

# Базовые проверки из условия работы.
assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

# Проверки варианта 1: строго больше порога.
assert select_numbers([-5, 0, 2, 5], 2) == [5]
assert select_numbers([], 2) == []

# Граница условия не включается: число, равное порогу, отбрасывается.
assert select_numbers([-5, 0, 2, 5], 5) == []
assert select_numbers([5, 6], 5) == [6]

# Повторы подходящего значения сохраняются.
assert select_numbers([-5, 0, 5, 5], 2) == [5, 5]

# Исходный список после вызова не изменяется.
source = [-5, 0, 2, 5]
saved = source[:]
select_numbers(source, 2)
assert source == saved

# Дробное среднее сравниваем с допуском.
assert abs(average([1, 2]) - 1.5) < 1e-9

print("Базовые проверки пройдены")
