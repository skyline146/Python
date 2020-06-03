# Написати рекурсивну процедуру перекладу натурального числа з десяткової системи числення в N-річної.
# Значення N в основній програмі вводиться з клавіатури (2 ≤ N ≤ 16).
def Func(a, n):
    if a == 0:
        return ""
    else:
        if a % n == 10:
            return "A" + Func(int(a / n), n)
        elif a % n == 11:
            return "B" + Func(int(a / n), n)
        elif a % n == 12:
            return "C" + Func(int(a / n), n)
        elif a % n == 13:
            return "D" + Func(int(a / n), n)
        elif a % n == 14:
            return "E" + Func(int(a / n), n)
        elif a % n == 15:
            return "F" + Func(int(a / n), n)
        else:
            return str(a % n) + Func(int(a / n), n)


n = int(input("Введите в какую систему исчисления переводить: "))
a = int(input("Введите число: "))
list_str = list(Func(a, n))
list_str.reverse()
str1 = ""
for i in list_str:
    str1 += i
print(str1)
