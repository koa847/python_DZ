class Worker ():

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position (Worker):

    def get_full_name (self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income (self):
        total_income = 0
        x = self._income
        for _, i in x.items():
            total_income += i
        return total_income


if __name__ == "__main__":
    worker_1 = Position("Александр", "Козлов", "продавец", {"wage": 100, "bonus": 20})
    worker_2 = Position("Владислв", "Баранов", "консультант", {"wage": 200, "bonus": 30})

    print(f'Сотрудник {worker_1.get_full_name()}, за отчетный период получил: {worker_1.get_total_income()}')
    print(f'Сотрудник {worker_2.get_full_name()}, за отчетный период получил: {worker_2.get_total_income()}')