# normalize.py
# Нормализация текста: убрать пробелы по краям и сжать внутренние до одного.

text = input("Введите текст: ")

original_length = len(text)
normalized = " ".join(text.split())
new_length = len(normalized)
word_count = len(normalized.split())

print(f"Исходная длина: {original_length}")
print(f"Новая длина: {new_length}")
print(f"Нормализованный текст: {normalized}")
print(f"Количество слов: {word_count}")
