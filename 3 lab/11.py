# Перевірити, чи є число простим.
a = int(input("Введите число: "))
i = 2
n = 0
while i < a:
    if a % i == 0:
        n += 1
    if n > 2:
        break
    i += 1
if n > 2:
    print("Число не простое!")
else:
    print("Число простое!")