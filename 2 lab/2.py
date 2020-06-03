# Дано три цілих числа. Знайти кількість додатних чисел в початковому наборі.
Array = [0, 0, 0]
k = 0
for i in range(0, 3):
    Array[i] = int(input("Введите число :"))
for i in range(0, 3):
    if(Array[i] > 0):
        k += 1
print(k)