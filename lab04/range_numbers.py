a = int(input("Первое число a: "))
b = int(input("Второе число b: "))

if a <= b:
    step = 1
else:
    step = -1

for number in range(a, b + step, step):
    print(number)
