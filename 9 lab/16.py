# 16. Даний рядковий файл, який містить дати в форматі, описаному в завданні 14.
# Створити новий рядковий файл, в якому дати з вихідного файлу розташовувалися б в порядку спадання.

f = open('files/4_1.txt')
Array = [[line.rstrip()] for line in f]
Array2 = []
k = 0
for i in Array:
    str1 = str(i)
    for j in range(0, len(str1)):
        if str1[j] == '/':
            k += 1
            if k == 2:
                Array2.append(str1[j+1:len(str1)-2])
                k = 0
f = open('files/4_2.txt', 'w')
Array2.sort()
Array2.reverse()
for i in Array2:
    f.write(str(i)+'\n')