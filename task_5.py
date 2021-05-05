class Stationery():
    def __init__(self, titel):
        self.titel = titel

    def drow(self):
        print("Запуск отрисовки", end=" ")


class Pen(Stationery):
    def drow(self):
        super(Pen, self).drow()
        print("рисует ручкой")


class Pencil(Stationery):
    def drow(self):
        super(Pencil, self).drow()
        print("рисует карандашом")


class Handle(Stationery):
    def drow(self):
        super(Handle, self).drow()
        print("рисует маркером")


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.drow()
pencil.drow()
handle.drow()