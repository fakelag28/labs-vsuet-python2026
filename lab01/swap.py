print("Обмен названиями двух аудиторий")

first_room = input("Первая аудитория: ")
second_room = input("Вторая аудитория: ")

print(f"Исходные значения: first_room = {first_room}, second_room = {second_room}")

temp_room = first_room
first_room = second_room
second_room = temp_room

print(f"После обмена: first_room = {first_room}, second_room = {second_room}")
