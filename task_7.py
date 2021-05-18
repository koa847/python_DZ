import re

class ComplexNumber:
    def __init__(self, number):
        self.number = number
        c_n = []
        pattern = re.compile(r'([-]*\d+)([+-])(\d+)i$')
        r = pattern.findall(self.number)
        for el in r[0]:
            c_n.append(el)
        self.real_part = int(c_n[0])
        self.imaginary_part = int(f'{c_n[1]}{c_n[2]}' if c_n[1] == '-' else f'{c_n[2]}')

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.imaginary_part + other.imaginary_part
        return ComplexNumber(f'{str(real)}{str(imaginary)}i' if imaginary < 0 else f'{str(real)}+{str(imaginary)}i')
    #
    def __mul__(self, other):
        real = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return ComplexNumber(f'{str(real)}{str(imaginary)}i' if imaginary < 0 else f'{str(real)}+{str(imaginary)}i')

    def __str__(self):
        return self.number


if __name__ == '__main__':
    number_1 = ComplexNumber('-2-8i')
    number_2 = ComplexNumber('-6+8i')
    print(number_1)
    print(number_2)
    print(number_1 + number_2)
    print(number_1 * number_2)



