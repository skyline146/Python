# 1. Дано ім'я файлу і ціле число N (> 1). Створити файл цілих чисел з такою назвою
# і записати в нього N перших позитивних парних чисел (2, 4, ...).

n = int(input())
i = 2
try:
    f = open('files/1.txt', 'w')
except FileNotFoundError:
    print("Error!")
except FileExistsError:
    print("Error!")
while n >= 1:
    f.write(str(i) + '\n')
    n -= 1
    i += 2