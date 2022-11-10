import math

class Rational:
    # numerator denominator
    def __init__(self, numerator: int, denominator: int):
        if not numerator or not denominator:
            raise ValueError

        # if not isinstance(numerator, int) or not isinstance(denominator, int):
        #     raise TypeError
        self.whole_number = 0
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        if self.whole_number > 0 :
            wn = str(self.whole_number) + " "
        else:
            wn = ""
        return f"{wn}{int(self.numerator)}/{int(self.denominator)}"

    def calculate(self):
        return self.numerator / self.denominator

    def reduce_fraction(self):
        __diwader = math.gcd(self.numerator, self.denominator)
        self.numerator /= __diwader
        self.denominator /= __diwader
        if self.numerator / self.denominator >= 1:
            self.whole_number = int(self.numerator // self.denominator)
            self.numerator %= self.denominator



    # comparison
    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.calculate() > other.calculate()

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.calculate() < other.calculate()

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.calculate() >= other.calculate()

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.calculate() <= other.calculate()

    # adding
    def __add__(self, other):
        if isinstance(other, Rational):
            __num1 = self.numerator
            __num2 = other.numerator
            __den1 = self.denominator
            __den2 = other.denominator
            # gcd - greatest common devisor, lcm - least common multiple
            gcd = math.gcd(__den1, __den2)
            lcm = (__den1 * __den2) // math.gcd(__den1, __den2)
            __ration = Rational(int(__num1 * (lcm / __den1) + __num2 * (lcm / __den2)), lcm)
            __ration.reduce_fraction()
            return __ration
        return NotImplemented


    def __radd__(self, other):
        if isinstance(other, Rational):
            __num1 = self.numerator
            __num2 = other.numerator
            __den1 = self.denominator
            __den2 = other.denominator
            # gcd - greatest common devisor, lcm - least common multiple
            gcd = math.gcd(__den1, __den2)
            lcm = (__den1 * __den2) // math.gcd(__den1, __den2)
            __ration = Rational(int(__num1 * (lcm / __den1) + __num2 * (lcm / __den2)), lcm)
            __ration.reduce_fraction()
            return __ration
        return NotImplemented


    # multypling
    def __mul__(self, other):
        pass


"""2) Создайте класс «Правильная дробь» и реализуйте методы сравнения,
сложения, вычитания и произведения для экземпляров этого класса."""