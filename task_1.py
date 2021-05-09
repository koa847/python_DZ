class Matrix():

    def __init__(self, list_lists):
        self.list_lists = list_lists

    def __str__(self):
        msg = ''
        for lists in self.list_lists:
            for el in lists:
                msg += f'{el}  '
            msg = f'{msg}\n'
        return msg

    def __add__(self, other):
        col_list = []
        if len(self.list_lists) == len(other.list_lists):
            col = 0
            for lists in self.list_lists:
                row = 0
                row_list = []
                if len(lists) == len(other.list_lists[col]):
                    for el in lists:
                        row_list.append(el + other.list_lists[col][row])
                        row += 1
                    col_list.append(row_list)
                    col += 1
                else: return 'Сложение матриц осуществляется только одинакового размера'
            return Matrix(col_list)
        else: return 'Сложение матриц осуществляется только одинакового размера'


mtx_1 = Matrix([[31, 22, 5], [37, 43, 0], [51, 86, 12]])
mtx_2 = Matrix([[4, 5, 8], [9, 3, 6], [7, 0, 12]])
mtx_4 = Matrix([[1, 2], [3, 4], [5,6]])
mtx_5 = Matrix([[7, 8], [9, 10], [11, 12]])
mtx_3 = mtx_1 + mtx_2
print(mtx_3)
print(mtx_1)
print(mtx_1 + mtx_4)
print(mtx_4 + mtx_5)
