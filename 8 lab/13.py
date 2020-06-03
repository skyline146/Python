# Скласти опис класу для представлення часу. Передбачити можливості установки часу і зміни його окремих полів
# (година, хвилина, секунда) з перевіркою допустимості вводяться значень.
# У разі неприпустимих значень полів викидаються виключення. Створити методи зміни часу на задану кількість годин, хвилин і секунд.

class Time:
    seconds = 0
    hours = 0
    minutes = 0
    new_seconds = 0
    new_minutes = 0
    new_hours = 0
    def set(self):
        while True:
            self.seconds = int(input())
            self.minutes = int(input())
            self.hours = int(input())
            if self.seconds < 0 or self.seconds > 59 or self.hours < 0 or self.minutes < 0 or self.minutes > 59:
                print("Your values out of range, please enter again!")
            else:
                break
    def changeTime(self):
        print("Enter how much change the values: ")
        self.new_seconds = int(input())
        self.new_minutes = int(input())
        self.new_hours = int(input())
        self.seconds += self.new_seconds
        self.minutes += self.new_minutes
        self.hours += self.new_hours


TimeObject = Time()
TimeObject.set()
a = int(input("If you want to change the values, enter 1, else - 0: "))
if a == 1:
    TimeObject.changeTime()
print(TimeObject.seconds)
print(TimeObject.minutes)
print(TimeObject.hours)