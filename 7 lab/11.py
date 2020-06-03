# У програмі задані місяць і рік двох дат. Користувач вводить ще одну дату (тільки місяць і рік).
# Визначити, чи належить третя дата діапазону від першої дати до другої включно. Завдання вирішити з використанням структури даних.

date2 = [8, 2019]
date1 = [5, 2018]
while True:
    dateTest = []
    dateTest.append(int(input()))
    dateTest.append(int(input()))
    if dateTest[0] > 12 or dateTest[0] < 1:
        print("Enter real number of month!")
    else:
        break

if dateTest[1] == date1[1] or dateTest[1] == date2[1]:
    if dateTest[1] == date1[1]:
        if date1[0] <= dateTest[0]:
            print("In range!")
        else:
            print("Out of range!")
    if dateTest[1] == date2[1]:
        if date2[0] >= dateTest[0]:
            print("In range!")
        else:
            print("Out of range!")
else:
    print("Out of range!")