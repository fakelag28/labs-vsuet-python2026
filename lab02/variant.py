total = int(input("Количество студентов: "))
capacity = int(input("Мест в автобусе: "))

full = total // capacity
remainder = total % capacity
buses = (total + capacity - 1) // capacity

print(f"Полностью заполненных автобусов: {full}")
print(f"Остаток студентов: {remainder}")
print(f"Минимальное число автобусов: {buses}")
