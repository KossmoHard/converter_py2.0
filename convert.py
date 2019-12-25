import re
import os


class Convert:

    def __init__(self):
        self.roman = {  # Словарь для конвертирования из римских чисел.
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        self.arab = {   # Словарь для конвертирования из арабских чисел.
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }


class ArabConvert(Convert):

    def regular_check(self, roman_number):
        regex = re.compile(r'^.*(.)(\1)(\1)(\1).*$')  # Условие для выполнения регулярного выражения.
                                                      # Согласно условию в римском числе не может стоять 4 одинаковые цифры подряд.
        if regex.match(roman_number):                 # Регулярное выражение по поиску соответствий условию в веденных римских числах.
            print("Invalid number format.")

            return False

        return True


    def get_roman(self, roman_number):
        storage = 0
        result = 0
        try:    # Исключение при вводе не корректных данных
            if self.regular_check(roman_number):
                for number in roman_number:

                    roman_number = self.roman[number]
                    if roman_number < storage:
                        result += storage
                        storage = roman_number
                    elif roman_number > storage:
                        if storage == 0:
                            storage = roman_number
                        else:
                            result += roman_number - storage
                            storage = 0
                    elif roman_number == storage:
                        result += roman_number + storage
                        storage = 0

        except KeyError:
            print("Invalid input")
            return None

        return result + storage


class RomanConvert(Convert):

    def get_number(self, num):  # Метод определает каким спопособо конвертировать числа до 3999 вызывается метод default_roman
        num = int(num)

        if num <= 3999:
            return self.default_roman(num)
        else:
            return self.no_default_roman(num)

    def default_roman(self, num):   # Метод конвертирование арабских чисел <= 3999
        number_arab = ''

        for ar, rm in self.arab.items():
            while num >= ar:
                number_arab += self.arab[ar]
                num -= ar
        return number_arab

    def no_default_roman(self, num):    # Метод конвертирование арабских чисел >= 3999
        num = str(num)[::-1]
        roman = ''
        num_result = [num[i:i + 3] for i in range(0, len(num), 3)]

        for j in num_result[::-1]:
            num = int(j[::-1])
            if num > 0:
                roman += self.default_roman(num)
                roman += ' '
            else:
                roman += 'M'

        return roman


def start():
    roman = RomanConvert()  # Конвертирование из арабских чисел в римские
    arab = ArabConvert()    # Конвертирование из римских в арабские, корректно работает до MMMCMXCIX / 3999
    start_convert = True    # Переменная-флаг в зависимости от значения которой будет выполняться основной цикл программы или нет.

    while start_convert:
        check_exit = True
        num = input('Enter a Roman or Arabic Number: ')

        if num.isdigit():
            print('Roman number: ', roman.get_number(num))
        else:
            print('Arab number: ', arab.get_roman(num))

        while check_exit:   # Цикл для выхода из программы по условию что флаг check_exit == False
            exit_convert = input('Exit (y/n)?: ')

            if exit_convert == 'y':
                start_convert = False
                check_exit = False
            elif exit_convert == 'n':
                check_exit = False
            else:
                print('Invalid input')


start()
