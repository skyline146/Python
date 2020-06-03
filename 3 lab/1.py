# У квадратній матриці відняти останній рядок з усіх рядків. Матрицю заповнити випадковими числами.
import random as r
n = int(input("Введите размер матрицы: "))
Array = [[r.randint(1, 10) for i in range(n)] for i in range(n)]
print(Array)
i = n-2
while i >= 0:
    for j in range(0, n):
        Array[i][j] -= Array[n-1][j]
    i -= 1
print(Array)