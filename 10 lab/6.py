# 6. Дано два файли довільного типу. Поміняти місцями їх вміст.

try:
    str1 = open('files/2_1.txt', 'r').read()
except:
    print("Error!")

try:
    str2 = open('files/2_2.txt', 'r').read()
except:
    print("Error!")

try:
    f = open('files/2_1.txt', 'w').write(str2)
except:
    print("Error!")

try:
    f = open('files/2_2.txt', 'w').write(str1)
except:
    print("Error!")