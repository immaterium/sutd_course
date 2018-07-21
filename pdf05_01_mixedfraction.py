from pdf04_02_fraction import Fraction
# inherits the earlier Fraction class, and overwrites part of it 

class MixedFraction(Fraction):
    def __init__(self, *args):
        if len(args) > 2:
            super().__init__(args[0] * args[2] + args[1], args[2])
        elif len(args) == 2:
            super().__init__(args[0], args[1])
        else:
            super().__init__(0,1)

    def get_three_numbers(self):
        if self.numerator > self.denominator:      
            whole = self.numerator//self.denominator
        else:
            whole = 0
            numer = self.numerator % self.denominator
            denominator = self.denominator
            return whole, numer, denominator

    # def get_three_numbers(self):
    #     if self.numerator > self.denominator:
    #         wholenum = self.numerator // self.denominator
    #         numer = (self.numerator % self.denominator)
    #         denom = self.denominator
    #         return (wholenum, numer, denom)
    #     else:
    #         pass

    def __add__(self,other):
        return MixedFraction(super().__add__(self,other))
    
    def __str__(self):
        whole, numer, denom = self.get_three_numbers()
        if whole != 0:
            return "{:d} {:d}/{:d}".format(whole, numer, denom)
        else:
            return super().__str__()
    
if __name__ == "__main__":

    mf1 = MixedFraction(3,2)
    assert mf1.numerator == 3 and mf1.denominator == 2

    mf2 = MixedFraction(1,1,2)
    assert mf1.numerator == 3 and mf1.denominator == 2

# if __name__ == "__main__":
#     mf1 = MixedFraction(3, 2)
#     assert mf1.numer == 3 and mf1.denom == 2
#     mf2 = MixedFraction(1, 1, 2)
#     assert mf1.numer == 3 and mf1.denom == 2
#     nums = mf2.get_three_numbers()
#     assert nums[0] == 1 and nums[1] == 1 and nums[2] == 2
#     print(mf2)
#     a = MixedFraction(1, 2, 4) # 3/2
#     print(a.numer, a.denom)
#     assert a.numer == 3 and a.denom == 2
#     b = MixedFraction(3, 1, 2) # 7/2
#     c = a + b
#     assert c.numer == 5 and c.denom == 1
#     d = a-b
#     assert d.numer == -2 and c.denom == 1
#     e = a*b
#     assert e.numer == 21 and e.denom == 4
#     assert a != b
#     b = MixedFraction(3, 2)
#     assert a == b
#     assert a <= b
#     b = MixedFraction(5, 2)
#     assert a < b
#     print(a)
