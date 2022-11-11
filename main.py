"""Домашнее задание
1) Создайте класс «Прямоугольник», у которого присутствуют два поля
(ширина и высота). Реализуйте метод сравнения прямоугольников по
площади. Также реализуйте методы сложения прямоугольников (площадь
суммарного прямоугольника должна быть равна сумме площадей
прямоугольников, которые вы складываете). Реализуйте методы
умножения прямоугольника на число n (это должно увеличить площадь
базового прямоугольника в n раз).
2) Создайте класс «Правильная дробь» и реализуйте методы сравнения,
сложения, вычитания и произведения для экземпляров этого класса."""
import rectangle
import rational


def test(x, y):
    # print(x > y)
    # print(x < y)
    # print(x >= y)
    # print(x <= y)
    #
    print(x + y)
    # print(y + x)
    #
    # print(x * 3)
    # print(y * 2)


def main():
    # rectangle
    # rect1 = rectangle.Rectangle(2, 3)
    # rect2 = rectangle.Rectangle(3, 4)
    # test(rect1, rect2)
    # print(rect1 > rect2)
    # print(rect1 < rect2)
    # print(rect1 >= rect2)
    # print(rect1 <= rect2)
    #
    # print(rect1 + rect2)
    # print(rect2 + rect1)
    #
    # print(rect1 * 3)
    # print(rect2 * 2)
    print("=============================")
    # rational
    rat1 = rational.Rational(49, 30)
    rat2 = rational.Rational(44, 45)
    test(rat1, rat2)






if __name__ == '__main__':
    main()


"""import math

class Rational:

    def __init__(self, a, b):
        if not isinstance(a, int):
            raise TypeError()

        if not isinstance(b, int):
            raise TypeError()

        if not b:
            raise ZeroDivisionError()

        self.__a = a
        self.__b = b

    def __mul__(self, other):
        if isinstance(other, int):
            return Rational(self.__a * other, self.__b)

        if isinstance(other, Rational):
            return Rational(self.__a * other.__a, self.__b * other.__b)

        raise TypeError()

    def __add__(self, other):
        if isinstance(other, int):
            return Rational(self.__a + self.__b * other, self.__b)

        if isinstance(other, Rational):
            return Rational(self.__a * other.__b + other.__a * self.__b, self.__b * other.__b)

        raise TypeError()

    def __str__(self):
        sign = '-' if self.__a * self.__b < 0 else ''

        if self.__a == self.__b:
            return '1'
        tmp = math.gcd(self.__a, self.__b)
        a = abs(self.__a // tmp)
        b = abs(self.__b // tmp)

        if a < b:
            return f'{a}/{b}'

        if not a % b:
            return f'{a // b}'

        return f'{sign}{a // b} {a - a // b * b}/{b}'


x1 = Rational(1, 2)
x2 = Rational(2, 4)
x3 = Rational(8, 8)

res = x1 + x2 + x3
print(res)"""