# swap.py
# Обязательное задание 4. Обмен значениями двух аудиторий.
# Обмен выполняем через третью (временную) переменную.

print("Обмен названиями двух аудиторий")

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

# Исходные значения.
print(f"Исходные значения: first_room = {first_room}, second_room = {second_room}")

# Обмен через третью переменную.
temp_room = first_room
first_room = second_room
second_room = temp_room

# Результат обмена.
print(f"После обмена: first_room = {first_room}, second_room = {second_room}")
