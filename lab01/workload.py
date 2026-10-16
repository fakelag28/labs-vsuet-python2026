print("Учебная нагрузка за неделю")
print("Введите данные по двум предметам и доступное время.")

subject1 = input("Название предмета 1: ")
lessons1 = int(input("Количество занятий по предмету 1: "))
minutes1 = int(input("Продолжительность занятия 1 (минут): "))

subject2 = input("Название предмета 2: ")
lessons2 = int(input("Количество занятий по предмету 2: "))
minutes2 = int(input("Продолжительность занятия 2 (минут): "))

available_hours = float(input("Доступное время на неделю (часов): "))

if lessons1 < 0 or lessons2 < 0:
    print("Ошибка: количество занятий не может быть отрицательным.")
    raise SystemExit(1)
if minutes1 <= 0 or minutes2 <= 0:
    print("Ошибка: продолжительность занятия должна быть положительной.")
    raise SystemExit(1)

time1_minutes = lessons1 * minutes1
time2_minutes = lessons2 * minutes2

total_minutes = time1_minutes + time2_minutes
total_hours = total_minutes / 60

free_hours = available_hours - total_hours
four_weeks_hours = total_hours * 4

if available_hours < total_hours:
    print("Ошибка: доступного времени меньше суммарной нагрузки.")
    raise SystemExit(1)

print()
print("=" * 44)
print("Расчёт учебной нагрузки")
print("=" * 44)
print(f"{subject1}: {time1_minutes} мин")
print(f"{subject2}: {time2_minutes} мин")
print(f"Общая нагрузка: {total_minutes} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {free_hours:.2f} ч")
print(f"Нагрузка за 4 недели: {four_weeks_hours:.2f} ч")
print("=" * 44)
