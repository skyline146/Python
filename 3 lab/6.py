# Дано список цілих чисел. Підрахувати, скільки разів в ньому зустрічається кожне число. Список заповнити випадковими числами.
import random as r
n = int(input("Введите кол-во чисел: "))
print("Введите промежуток для генерации случайных чисел: ")
from_ = int(input("От: "))
to_ = int(input("До: "))
g = from_
l = 0
Array = [r.randint(from_, to_) for i in range(n)]
for i in range(from_, to_ + 1):
    l += 1
ArrayExample = [0 for i in range(l)]
for i in range(0, l):
    if from_ <= to_:
        ArrayExample[i] = from_
    from_ += 1
k = 0
print(Array)
for j in range(0, l):
    k = 0
    for i in range(0, n):
        if Array[i] == ArrayExample[j]:
            k += 1
    if g <= to_:
        print("Цифра "+str(g)+": "+str(k)+" раз(а).")
    g += 1