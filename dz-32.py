class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def gcd(x, y):

        while y != 0:
            x, y = y, x % y
        return x

    def simplify(self):
        common_divisor = self.gcd(self.a, self.b)
        self.a //= common_divisor
        self.b //= common_divisor

    def __mul__(self, other):
        if isinstance(other, Fraction):
            res_a = self.a * other.a
            res_b = self.b * other.b
            res_fraction = Fraction(res_a, res_b)
            return res_fraction

    def __add__(self, other):
        if isinstance(other, Fraction):
            res_a = self.a * other.b + other.a * self.b
            res_b = self.b * other.b
            res_fraction = Fraction(res_a, res_b)
            return res_fraction

    def __sub__(self, other):
        if isinstance(other, Fraction):
            res_a = self.a * other.b - other.a * self.b
            res_b = self.b * other.b
            res_fraction = Fraction(res_a, res_b)
            return res_fraction

    def __eq__(self, other):
        if isinstance(other, Fraction):
            self.simplify()
            other.simplify()
            return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        if isinstance(other, Fraction):
            result_a_self = self.a * other.b
            result_a_other = other.a * self.b
            return result_a_self > result_a_other

    def __lt__(self, other):
        if isinstance(other, Fraction):
            result_a_self = self.a * other.b
            result_a_other = other.a * self.b
            return result_a_self < result_a_other

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'
#
assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
