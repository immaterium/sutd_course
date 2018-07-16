from math import gcd

class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self._numerator = numerator
        self._denominator = denominator
        self.reduce()

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter 
    def numerator(self,val):
        if isinstance(val,int):
            self._numerator = val
    
    @property
    def denominator(self):
        return self._denominator

    @denominator.setter 
    def denominator(self,val):
        if isinstance(val,int):
            if val > 0:
                self._denominator = val
            else:
                raise ValueError('number not allowed.')

# set_numerator..
# get_numerator..
# numerator = property(get_numerator,set_numerator)
# denominator = property(get_denominator,set_denominator)


    def reduce(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

    def __add__(self,other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return Fraction(a * d + b * c, b * d)

        # reduce will be done automatically because of init

    def __sub__(self,other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return Fraction(a * d - b * c, b * d)

    def __mul__(self,other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return Fraction(a * c, b * d)

    def __eq__(self,other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self,other):
        a = self.numerator
        b = self.denominator
        c = other.numerator
        d = other.denominator
        return a * d < b * c

    def __le__(self,other):
        return self == other or self < other

    def __gt__(self,other):
        return not(self <= other)

    def __gt__(self,other):
        return not(self < other)


f1 = Fraction(1,4)
f2 = Fraction(1,2)
f3 = f1 + f2
assert f3.numerator == 3 and f3.denominator == 4
f4 = Fraction(6,8)
assert f4.numerator == 3 and f3.denominator == 4

# f1 = Fraction(2,4)
# assert f1.numerator == 1 and f1.denominator == 2


# f2 = Fraction(3,4)
# f3 = f1 + f2
# assert f3.numerator == 5 and f3.denominator == 4

# f4 = f3 - f1
# assert f4.numerator == 3 and f4.denominator == 4

# f5 = f1 * f2
# assert f5.numerator == 3 and f5.denominator == 8

# assert f4 == f2
# assert f5 < f1

# print(f1._numerator)