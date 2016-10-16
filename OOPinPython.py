class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num
        return first_num == second_num


def gcd(m, n):
    while m % n is not 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

my_fraction = Fraction(3,5)
print(my_fraction)

f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2

print (f3)

print (f1 == f2)