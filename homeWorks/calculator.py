class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return self.num1 + other.num2

    def __sub__(self, other):
        return self.num1 - other.num2

    def __mul__(self, other):
        return self.num1 * other.num2

    def __truediv__(self, other):
        return self.num1 / other.num2
