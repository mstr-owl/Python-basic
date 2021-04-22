class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            res = divider / denominator
            return res
        except ZeroDivisionError:
            res = "Делить на ноль нельзя"
            return res


div = DivisionByNull(10, 1000)
print(DivisionByNull.divide_by_null(50, 0))
print(DivisionByNull.divide_by_null(100, 100000))
print(div.divide_by_null(525, 0))
print(div.divide_by_null(345, 5))
