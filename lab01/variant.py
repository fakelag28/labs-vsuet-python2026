print("Оформление заказа (вариант 1: Канцелярия)")

order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")

item1_name = input("Название позиции 1: ")
item1_count = int(input("Количество позиции 1: "))
item1_price = float(input("Цена единицы позиции 1 (руб.): "))

item2_name = input("Название позиции 2: ")
item2_count = int(input("Количество позиции 2: "))
item2_price = float(input("Цена единицы позиции 2 (руб.): "))

delivery = float(input("Стоимость доставки (руб.): "))
paid = float(input("Внесённая сумма (руб.): "))

item1_cost = item1_count * item1_price
item2_cost = item2_count * item2_price
goods_cost = item1_cost + item2_cost
total_cost = goods_cost + delivery
total_count = item1_count + item2_count
change = paid - total_cost

print()
print(f"=== Заказ: {order_name} ===")
print(f"Заказчик: {customer}")
print(f"{item1_name} | {item1_count} | {item1_price:.2f} | {item1_cost:.2f}")
print(f"{item2_name} | {item2_count} | {item2_price:.2f} | {item2_cost:.2f}")
print(f"Стоимость позиции «{item1_name}»: {item1_cost:.2f} руб.")
print(f"Стоимость позиции «{item2_name}»: {item2_cost:.2f} руб.")
print(f"Стоимость товаров без доставки: {goods_cost:.2f} руб.")
print(f"Стоимость доставки: {delivery:.2f} руб.")
print(f"Общая сумма с доставкой: {total_cost:.2f} руб.")
print(f"Общее количество единиц: {total_count}")
print(f"Сдача: {change:.2f} руб.")
