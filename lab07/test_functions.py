from functions import average, normalize_text, select_numbers, sum_digits

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert abs(average([1, 2]) - 1.5) < 1e-9
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""
numbers = [-5, 0, 2, 3, 5, 5]
original = numbers.copy()
assert select_numbers(numbers, 2) == [3, 5, 5]
assert select_numbers([], 2) == []
assert numbers == original
print("Проверки пройдены")
