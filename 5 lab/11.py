# Описати рекурсивную функцію Palindrome (S) логічного типу, яка повертає True,
# якщо рядок S є паліндромом (тобто читається однаково зліва направо і справа наліво), і False в іншому випадку.
# Оператор циклу в тілі функції не використовувати. Вивести значення функції Palindrome для п'яти довільних рядків.
def recur(str1, i):
    if i < 0:
        return ""
    else:
        return str1[i] + recur(str1, i - 1)


def palindrome(s):
    if s == recur(s, len(s)-1):
        return True
    else:
        return False


Array = []
for i in range(0, 1):
    Array.append(input())
for i in Array:
    print(palindrome(i))
