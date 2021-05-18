from abc import ABC, abstractmethod


class Warehouse:
    warehouse = {}

    @classmethod
    def into_warehouse(cls, office_equipment):
        try:
            types = []
            names = []
            name = office_equipment.__class__.__qualname__
            brend = office_equipment.brend
            for el in cls.warehouse.keys(): types.append(el)
            if name in types:
                for ex in cls.warehouse[name].keys(): names.append(ex)
                if brend in names:
                    cls.warehouse[name][brend] += 1
                else: cls.warehouse[name][brend] = 1
            else: cls.warehouse[name] = {brend: 1}
            office_equipment.location = "склад"
        except: print("На склад могут быть отправленны только экземпляры оргтехники")

    @classmethod
    def from_warehouse(cls, office_equipment,  where):
        try:
            types = []
            names = []
            name = office_equipment.__class__.__qualname__
            brend = office_equipment.brend
            for el in cls.warehouse.keys(): types.append(el)
            if name in types:
                for ex in cls.warehouse[name].keys(): names.append(ex)
                if brend in names:
                    col = int(cls.warehouse[name][brend])
                    col -= 1
                    cls.warehouse[name][brend] = col
                    office_equipment.location = where
                    if cls.warehouse[name][brend] == 0:
                        del cls.warehouse[name][brend]
                        if not cls.warehouse[name]:
                            del cls.warehouse[name]
                else: print(f'На складе нет {name} бренда: {brend}')
            else: print(f'На складе нет {name}')
        except: print("Со склада можно забирать только экземпляры оргтехники")

    def __str__(self):
        msg = f'На складе находится: \n'
        for k, v in self.warehouse.items():
            msg += f'   {k} а именно:\n'
            for brend, quant in self.warehouse[k].items():
                msg += f'      {brend} в колличестве: {quant} шт.\n'
        return msg


class OfficeEquipment():
    def __init__(self, brend, location="магазин"):
        self.brend = brend
        self.location = location

    def __str__(self):
        str = f'модель: {self.brend}, находится: {self.location}'
        self.characteristic()
        return str + '\n'

    @abstractmethod
    def characteristic(self):
        pass

class Printer(OfficeEquipment):
    def characteristic(self):
        print(f'{self.__class__.__qualname__} используется для печати,', end=' ')


class Scanner(OfficeEquipment):
    def characteristic(self):
        print(f'{self.__class__.__qualname__} используется для сканирования.', end=' ')


class Copier(OfficeEquipment):
    def characteristic(self):
        print(f'{self.__class__.__qualname__} используется для копирования.', end=' ')


printer_1 = Printer('HP')
scanner_1 = Scanner('HP')
printer_2 = Printer('Xerox')
scanner_2 = Scanner('HP')
copier_1 = Copier('HP')

if __name__ == '__main__':
    print(printer_1)
    Warehouse.into_warehouse(printer_1)
    Warehouse.into_warehouse(scanner_1)
    Warehouse.into_warehouse(printer_2)
    Warehouse.into_warehouse(scanner_2)
    print(Warehouse())
    Warehouse.from_warehouse(printer_1, "офис")
    print(Warehouse())
    print(printer_1)
    Warehouse.from_warehouse(copier_1, "офис")
    Warehouse.from_warehouse(scanner_1, 'бухгалтерия')
    print(Warehouse())
    print(scanner_1)
    Warehouse.into_warehouse(copier_1)
    Warehouse.into_warehouse(printer_1)
    Warehouse.into_warehouse(printer_1)
    print(Warehouse())
    Warehouse.into_warehouse('Printer')
    Warehouse.from_warehouse('Printer', "офис")