# Даний рядок. Отримайте новий рядок, вставивши між кожними двома символами вихідної рядки символ *. Виведіть отриманий рядок.
strExample = ""
strlist = list(input())
a = 1
while a < len(strlist)-1:
    strlist[a] += '*'
    a += 2
for i in strlist:
    strExample += i
print(strExample)