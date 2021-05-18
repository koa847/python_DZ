class DivZero(Exception):
    msg = "Ошибка: делить на ноль запрещенно"

    @staticmethod
    def check_num(number):
        try: return True if number != 0 else True
        except ValueError: return False


def div_num():
    while True:
        num_1 = input('Введите число 1 или "stop" для выхода: ')
        if num_1 == 'stop': break
        num_2 = input('Ввидите число 2 или "stop" для выхода: ')
        if num_2 == 'stop': break
        try:
            if DivZero.check_num(num_2):
                result = float(num_1) / float(num_2)
                print(result)
        except: print(DivZero().msg)


if __name__ == '__main__':
    div_num()