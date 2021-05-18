class NumberList(Exception):
    msg = "Вводить нужно только числа"

    @staticmethod
    def check_num(number):
        return True if float(number) else False


def num():
    numbers = []
    while True:
        number = input('Введите число или "stop" для выхода: ')
        if number == 'stop': break
        try:
           if NumberList.check_num(number):
                numbers.append(float(number))
        except ValueError:
            print(NumberList().msg)
    print(numbers)


if __name__ == '__main__':
    num()