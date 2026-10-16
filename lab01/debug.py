print("Фрагмент А: сумма чисел 2 и 3")

first_text = "2"
second_text = "3"
print("Тип до преобразования:", type(first_text), type(second_text))

first = int(first_text)
second = int(second_text)
print("Тип после преобразования:", type(first), type(second))

sum_a = first + second
print("Результат А (сумма):", sum_a)

print()
print("Фрагмент Б: возраст через год")

age_text = input("Возраст: ")
print("Тип до преобразования:", type(age_text))

age = int(age_text)
print("Тип после преобразования:", type(age))

age_next_year = age + 1
print("Результат Б (возраст через год):", age_next_year)

print()
print("Фрагмент В: среднее трёх чисел")

first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Результат В (среднее):", average)
