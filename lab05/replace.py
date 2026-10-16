text = input("Введите текст: ")

count = text.count(":")
new_text = text.replace(":", "-")

print(f"Количество замен: {count}")
print(f"Новая строка: {new_text}")
