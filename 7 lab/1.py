# Даний рядок. Вивести окремі слова, що входять до нього, розділені пробілами, впорядкованими за алфавітом, в стовпчик.

str1 = input()
if str1[len(str1)-1] != " ":
    str1 += " "
String_Array = []
y = 0
for i in range(0, len(str1)):
    if str1[i] == " ":
        String_Array.append(str1[y:i])
        y = i+1
String_Array.sort()
for i in String_Array:
    print(i)