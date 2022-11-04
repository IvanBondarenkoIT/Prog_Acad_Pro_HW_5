class Rectangle:
    def __init__(self, wight: int | float, height: int | float):
        if not wight or not height:
            raise ValueError
        if isinstance(wight, int | float):
            raise TypeError

        self.wight = wight
        self.height = height

    def area(self):
        return self.wight * self.height

    # comparison
    def __gt__(self, other):
        if isinstance(other, Rectangle):
            raise NotImplemented
        return self.area() > other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            raise NotImplemented
        return self.area() < other.area()

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            raise NotImplemented
        return self.area() >= other.area()

    def __le__(self, other):
        if isinstance(other, Rectangle):
            raise NotImplemented
        return self.area() <= other.area()

    # adding
    def __add__(self, other):
        if isinstance(other, Rectangle):
            raise NotImplemented
        return self.area() + other.area()

    def __radd__(self, other):
        if isinstance(other, Rectangle):
            raise NotImplemented
        return self.area() + other.area()

    # multypling
    def __mul__(self, other):
        if isinstance(other, int | float):
            raise NotImplemented
        return self.area() * other

'''1) Создайте класс «Прямоугольник», у которого присутствуют два поля
(ширина и высота). Реализуйте метод сравнения прямоугольников по
площади. Также реализуйте методы сложения прямоугольников (площадь
суммарного прямоугольника должна быть равна сумме площадей
прямоугольников, которые вы складываете). Реализуйте методы
умножения прямоугольника на число n (это должно увеличить площадь
базового прямоугольника в n раз).'''