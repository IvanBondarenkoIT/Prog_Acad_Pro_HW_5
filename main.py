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


