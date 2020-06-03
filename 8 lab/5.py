# Створити клас з двома змінними. Додати конструктор з вхідними параметрами. Додати конструктор,
# не започатковано члени класу за замовчуванням. Додати деструкцію, що виводить на екран повідомлення про видалення об'єкта.

class Example:
    a = 0
    b = 0
    def init_2(self):
        self.a = 35
        self.b = 24
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __del__(self):
        print("Object was deleted!")


ObjectExample1 = Example(0, 0)
ObjectExample1.init_2()
ObjectExample2 = Example(3, 4)