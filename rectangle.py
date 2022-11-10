class Rectangle:
    def __init__(self, wight: int | float, height: int | float):
        if not wight or not height:
            pass
            #raise ValueError

        if isinstance(wight, int | float):
            pass
            #raise TypeError

        self.wight = wight
        self.height = height

    def area(self):
        return self.wight * self.height

    # comparison
    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area() >= other.area()

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()

    # adding
    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.area() + other.area()
        return NotImplemented


    def __radd__(self, other):
        if isinstance(other, Rectangle):
            return self.area() + other.area()
        return NotImplemented


    # multypling
    def __mul__(self, other):
        if isinstance(other, int | float):
            return self.area() * other
        return NotImplemented


'''1) Создайте класс «Прямоугольник», у которого присутствуют два поля
(ширина и высота). Реализуйте метод сравнения прямоугольников по
площади. Также реализуйте методы сложения прямоугольников (площадь
суммарного прямоугольника должна быть равна сумме площадей
прямоугольников, которые вы складываете). Реализуйте методы
умножения прямоугольника на число n (это должно увеличить площадь
базового прямоугольника в n раз).'''