# Створити абстрактний клас Figure з методами обчислення
# площі та периметра, а також методом, що виводить інформацію про фігуру на
# екран. Створити похідні класи: Rectangle (прямокутник), Circle (коло), Triangle
# (трикутник) зі своїми методами обчислення площі
# і періметра.Создать масив n фігур і вивести повну інформацію про фігури на екран.
from abc import abstractmethod


class Figure:
    @abstractmethod
    def perimetr(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def inform(self):
        pass
class Rectangle(Figure):
    a = 0
    b = 0
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a*self.b
    def perimetr(self):
        return 2*(self.a+self.b)
    def inform(self):
        print("Rectangle")

class Circle (Figure):
    R = 0
    def __init__(self,R):
        self.R = R
    def area(self):
        return 3.14*(self.R ** 2)
    def perimetr(self):
        return 23.14*(self.R)
    def inform(self):
        print("Circle")
class Triangle (Figure):
    a = 0
    b = 0
    c = 0
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        return self.a+self.b*self.c
    def perimetr(self):
        return self.a+self.b+self.c
    def inform(self):
        print("Triangle")
fig = [Rectangle(1,2),Circle(3),Triangle(1,2,3)]
fig[0].inform()
print(fig[0].area())
print(fig[0].perimetr())
fig[1].inform()
print(fig[1].area())
print(fig[1].perimetr())
fig[2].inform()
print(fig[2].area())
print(fig[2].perimetr())