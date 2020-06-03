# 11. Дано символьний файл, який містить принаймні один символ пробілу.
# Видалити всі його елементи, розташовані після останнього символу пробілу, включаючи і цей пробіл.

try:
    f = open('files/3.txt')
except FileNotFoundError:
    print("FileNotFoundError!")
except FileExistsError:
    print("FileExistsError!")
else:
    print("File opened successfully!")
str1 = f.read()
str2 = ""
for i in range(0, len(str1)):
    if str1[i] == ' ':
        str2 = str1[:i]
f = open('files/3.txt', 'w').write(str2)