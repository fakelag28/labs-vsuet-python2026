print("Анкета студента")
print("Ответьте, пожалуйста, на семь вопросов.")

surname = input("Фамилия: ")
name = input("Имя: ")
group = input("Группа: ")
city = input("Город: ")
age = int(input("Возраст (полных лет, от 1 до 120): "))
subject = input("Любимый предмет: ")
study_hours = float(input("Часов подготовки в неделю: "))

if age < 1 or age > 120:
    print("Ошибка: возраст должен быть от 1 до 120.")
    raise SystemExit(1)
if study_hours < 0:
    print("Ошибка: часы подготовки не могут быть отрицательными.")
    raise SystemExit(1)

full_name = name + " " + surname
age_in_four_years = age + 4
hours_in_four_weeks = study_hours * 4
hours_per_day = study_hours / 7

print()
print("=" * 44)
print("Карточка студента")
print("=" * 44)
print(f"Полное имя (имя фамилия): {full_name}")
print(f"Группа: {group}")
print(f"Город: {city}")
print(f"Возраст сейчас: {age} лет")
print(f"Возраст через 4 года: {age_in_four_years} лет")
print(f"Любимый предмет: {subject}")
print(f"Подготовка в неделю: {study_hours:.2f} ч")
print(f"Подготовка за 4 недели: {hours_in_four_weeks:.2f} ч")
print(f"В среднем в день: {hours_per_day:.2f} ч")
print("=" * 44)
