price = int(input("Цена одной тетради в рублях: "))
count = int(input("Количество тетрадей: "))
paid = int(input("Переданная сумма в рублях: "))

cost = price * count
change = paid - cost

print(f"Стоимость: {cost} руб.")
print(f"Сдача: {change} руб.")
