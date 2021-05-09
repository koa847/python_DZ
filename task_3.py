class Cell():
    def __init__(self, slot):
        self.slot = int(slot)

    def __str__(self):
        return f"У данной клетки колличество ячеек равно: {self.slot}"

    def __add__(self, other):
        return Cell(self.slot + other.slot)

    def __sub__(self, other):
        sub = self.slot - other.slot
        if sub > 0: return Cell(sub)
        else: print("Вычитание невозможно")

    def __mul__(self, other):
        return Cell(self.slot * other.slot)

    def __truediv__(self, other):
        return Cell(self.slot // other.slot)

    def __floordiv__(self, other):
        return Cell(self.slot // other.slot)

    def make_order(self, row):
        str = ''
        for cell in range(self.slot//row):
            for cl in range(row):
                str += "*"
            str+= "\n"
        for c in range(self.slot % row):
            str += "*"
        return str


cell_1 = Cell(12)
cell_2 = Cell (16)
cell_3 = Cell(8)

print(cell_1.make_order(5))
print(cell_2 - cell_3)
print(cell_1 / cell_3)
cell_4 = cell_1 + cell_3
print(cell_4.make_order(5))