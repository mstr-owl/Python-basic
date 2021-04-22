class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f"При сложении клеток,число ячеек общей клетки равно:{self.quantity + other.quantity}"

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'При вычетании клеток, число ячеек общей клетки равно: {sub}' if sub > 0 else 'Клеток больше нет'

    def __truediv__(self, other):
        return f"При произведении клеток, число ячеек общей клетки равно: {self.quantity // other.quantity}"

    def __mul__(self, other):
        return f"При делении клеток, число ячеек общей клетки равно: {self.quantity * other.quantity}"

    def make_order(self, row):
        result = ''
        for _ in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell_1 = Cell(52)
cell_2 = Cell(5)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(5))
