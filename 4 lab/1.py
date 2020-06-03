# Дано перший член і різницю арифметичної прогресії.
# Написати рекурсивну функцію для знаходження n-го члена прогресії і суми n перших членів прогресії.
def FuncN(d, n):
    if n == 0:
        return 0
    else:
        return d + FuncN(d, n-1)
def FuncSum(a1, an, n):
    return ((a1+an)/2)*n
a1 = int(input("Введите 1-й член прогресии: "))
d = int(input("Введите шаг прогресии: "))
n = int(input("Введите кол-во членов прогресии: "))
print(a1+FuncN(d,n-1))
print(FuncSum(a1, a1+FuncN(d, n-1), n))