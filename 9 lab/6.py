# 6. Дано два файли довільного типу. Поміняти місцями їх вміст.

str1 = open('files/2_1.txt', 'r').read()
str2 = open('files/2_2.txt', 'r').read()
f = open('files/2_1.txt', 'w').write(str2)
f = open('files/2_2.txt', 'w').write(str1)