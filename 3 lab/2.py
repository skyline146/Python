# По залишку від ділення цілої частини значення функції y = log (x² + ab) на 7 вивести день тижня.
# Значення змінних а, b, x отримати випадковим чином на зазначеному користувачем інтервалі.
import random as r
import math as m
print("Введите интервал для генерации случайных значений переменных: ")
from_ = int(input("От: "))
to_ = int(input("До: "))
a = r.randint(from_, to_)
b = r.randint(from_, to_)
x = r.randint(from_, to_)
y = int(m.log10(x*x + a*b))
print(y % 7)
if y % 7 == 1:
    print("Понедельник!")
elif y % 7 == 2:
    print("Вторник!")
elif y % 7 == 3:
    print("Среда!")
elif y % 7 == 4:
    print("Четверг!")
elif y % 7 == 5:
    print("Пятница!")
elif y % 7 == 6:
    print("Суббота!")
elif y % 7 == 0:
    print("Воскресенье!")