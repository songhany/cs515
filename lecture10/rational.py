class Rational:
    def __init__(self, n, d) -> None:
        self.numerator = n
        self.denominator = d

    def isZero(self):
        return self.numerator == 0

    def add(self, other):
        newNumerator = self.numerator * other.denominator \
                        + self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)

    def __add__(self, other):
        newNumerator = self.numerator * other.denominator \
                        + self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)

    def __eq__(self, other) -> bool:
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __ge__(self, other):
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self.numerator) + "/" + str(self.denominator)


r1 = Rational(3, 4)
r2 = Rational(3, 5)
print(r1)
print(r1 + r2)
print(r1 >= r2)
