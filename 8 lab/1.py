# 1. Створіть клас з ім'ям student, що містить поля: прізвище' \
#                      ' та ініціали, номер групи, успішність (масив з п'яти елементів).
# Створити масив з десяти елементів такого типу, впорядкувати записи
# за зростанням середнього бала. Додати можливість
# виведення прізвищ і номерів груп студентів, які мають оцінки, рівні тільки 4 або 5.
import random
class Student:
    surname = ""
    group = ""
    avg = 0
    Array = [0 for i in range(5)]
    def __init__(self,surname,group,Array):
        sum = 0
        self.surname = surname
        self.group = group
        self.Array = Array
        for i in range(0, len(self.Array)):
            sum += self.Array[i]
        self.avg = sum/5


Array = [Student("Student","141",[random.randint(1, 5) for i in range(5)]) for y in range(10)]
min = 0
index = 0
for i in range(len(Array)):
    m = i
    j = i + 1
    while j < len(Array):
        if Array[j].avg < Array[m].avg:
            m = j
        j = j + 1
    Array[i], Array[m] = Array[m], Array[i]
for i in range(len(Array)):
    print(Array[i].avg)