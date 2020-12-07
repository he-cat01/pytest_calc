class Calc:
    def __init__(self):
        pass

    @staticmethod
    def add(x1, x2):
        return x1 + x2

    @staticmethod
    def sub(x1, x2):
        return x1 - x2

    @staticmethod
    def multi(x1, x2):
        return x1 * x2

    @staticmethod
    def div(x1, x2):
        if not x2 == 0:
            return x1 / x2
        else:
            return ZeroDivisionError


if __name__ == '__main__':
    calc = Calc()
