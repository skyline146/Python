# Дано ціле число. Якщо воно є додатним, то відняти від нього 8; в іншому разі не змінювати його. Вивести отримане число.
a = int(input("Введите число: "))
if a > 0:
    print(a-8)
else:
    print(a)