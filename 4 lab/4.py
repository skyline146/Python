# Написати рекурсивну процедуру для виведення на екран цифр натурального числа у зворотному порядку.
def func(a):
    if int(a / 10) == 0:
        return str(a % 10)
    else:
        return str(a % 10) + " " + func(int(a / 10))


input_list = list(func(int(input())))
str1 = ""
for i in input_list:
    str1 += i
print(str1)
