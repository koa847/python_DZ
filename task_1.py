import time
import re

class Data:

    def __init__(self, data):
        self.data = data

    @classmethod
    def convert_date(cls, param):
        pattern = re.compile(r'(^\d{2})-(\d{2})-(\d{4}$)')
        r = pattern.findall(param)
        return "Неверный формат даты" if not r else r[0]

    @staticmethod
    def check_date(date):
        try:
            time.strptime(date, '%d-%m-%Y')
            return date
        except ValueError:
            return 'Дата введена не верно'


data_1 = Data('17-05-2021')
data_2 = Data("17.05.2021")

print(data_1.convert_date(data_1.data))
print(data_2.convert_date(data_2.data))
print(data_1.check_date(data_1.data))

print(Data.convert_date('17-05-2021'))
print(Data.convert_date('17.05.2021'))
print(Data.check_date('30-02-2021'))
