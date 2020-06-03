# Даний текст. Замінити всі входження найбільшої цифри її словесним написанням.

d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
str1 = input()
if str1[len(str1)-1] != " ":
    str1 += " "
Int_Array = []
y = 0
for i in range(0, len(str1)):
    if str1[i] == " ":
        Int_Array.append(int(str1[y:i]))
        y = i+1
max = Int_Array[0]
for i in Int_Array:
    if i > max:
        max = i
for i in range(0, len(Int_Array)):
    if Int_Array[i] == max:
        Int_Array[i] = d[max]
print(Int_Array)