text = input("Введите текст: ")

count = 0

for word in text.split():
    clean = word.strip(".,!?;:").lower()
    if clean == "":
        continue
    if clean.startswith("а"):
        print(clean)
        count += 1

if count == 0:
    print("Нет совпадений")

print(f"Количество: {count}")
