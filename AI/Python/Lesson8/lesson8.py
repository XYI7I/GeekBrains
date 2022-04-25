# coding: utf-8

# Основы языка Python.
# Занятие 8. Объектно-ориентированное программирование.  Полезные дополнения

# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. 
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
print("Урок 8. Задание 1.")
part1 = input('Выполнить задание 1? (Y/N)')
if part1.title() == 'Y':
    from datetime import date

    class Data:
        def __init__(self, day_month_year):
            self.day_month_year = str(day_month_year)

        @classmethod
        def extract(cls, day_month_year):
            my_date = []

            for i in day_month_year.split('-'):
                my_date.append(i)

            return int(my_date[0]), int(my_date[1]), int(my_date[2])

        @staticmethod
        def valid(day_month_year):
            day, month, year = map(int, day_month_year.split('-'))

            if 0 < day < 32:
                if 0 < month < 13:
                    if 0 < year < 2022:
                        if month == 4 or month == 6 or month == 9 or month == 11:
                            if 0 < day < 31:
                                pass
                            else:
                                return f'Для этого месяца число дней от 1 до 30'
                        elif month == 2:
                            if year % 4 == 0:
                                if day > 29:
                                    return f'Для февраля високосного года число дня от 1 до 29'
                                else:
                                    pass
                            else:
                                if day > 28:
                                    return f'Для февраля число дня от 1 до 28'
                                else:
                                    pass
                        return f'Правильный формат даты'
                    else:
                        return f'Неправильный год'
                else:
                    return f'Неправильный месяц'
            else:
                return f'Неправильный день'

        def __str__(self):
            return f'Введенная дата {Data.extract(self.day_month_year)}'

    current_date = date.today()
    print('Дата:', current_date)
    answer = ''
    while answer.title() != 'Y':
        inp_data = input('Введите дату в формате дд-мм-гггг: ')
        print(Data(inp_data))
        print(Data.extract(inp_data))
        print(Data.valid(inp_data))
        answer = input('Закончить выполнение задания 1? (Y/N)')
else:
    pass

print('***')

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
print("Урок 8. Задание 2.")

part2 = input('Выполнить задание 2? (Y/N)')
if part2.title() == 'Y':
    class DivByZero:
        def __init__(self, quot, div):
            self.div = div
            self.quot = quot

        @staticmethod
        def div_by_zero(quot, div):
            try:
                return (quot / div)
            except:
                return (f'Деление на ноль невозможно')

    answer = ''
    while answer.title() != 'Y':
        inp_quot = int(input('Введите частное: '))
        inp_div = int(input('Введите делитель: '))
        div = DivByZero(inp_quot, inp_div)
        print(DivByZero.div_by_zero(inp_quot, inp_div))
        answer = input('Закончить выполнение задания 2? (Y/N)')
else:
    pass
print('***')

# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере. 
# Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”. 
# При этом скрипт завершается, сформированный список выводится на экран.
print("Урок 8. Задание 3.")

part3 = input('Выполнить задание 3? (Y/N)')
if part3.title() == 'Y':

    class Error:
        def __init__(self, *args):
            self.my_list = []

        def input_list(self):

            while True:
                try:
                    list_var = input('Введите числовое значение и нажимайте "Enter"(Для выхода введите "stop")')
                    if list_var == 'stop':
                        return f'Текущий список - {self.my_list} \n '
                        return f'***'
                        pass
                    else:
                        list_int_var = int(list_var)
                        self.my_list.append(list_int_var)

                except:
                    print(f"Недопустимое значение (str или bool)")

    try_except = Error(1)
    print(try_except.input_list())

else:
    pass

print('***')

# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. 
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

print("Урок 8. Задание 4 - 6.")

part4 = input('Выполнить задания 4 - 6? (Y/N)')
if part4.title() == 'Y':

    class StoreMashines:

        def __init__(self, name, price, quantity, number_of_lists, *args):
            self.name = name
            self.price = price
            self.quantity = quantity
            self.numb = number_of_lists
            self.my_store_full = []
            self.my_store = []
            self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

        def __str__(self):
            return f'{self.name} цена {self.price} количество {self.quantity}'

        # @classmethod
        # @staticmethod
        def reception(self):
            # print(f'Для выхода - Q, продолжение - Enter')
            # while True:
            try:
                unit = input(f'Введите наименование ')
                unit_p = int(input(f'Введите цену за ед '))
                unit_q = int(input(f'Введите количество '))
                unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                print(f'Текущий список -\n {self.my_store}')
            except:
                return f'Ошибка ввода данных'

            print(f'Для выхода - Q, продолжение - Enter')
            q = input(f'---> ')
            if q == 'Q' or q == 'q':
                self.my_store_full.append(self.my_store)
                print(f'Весь склад -\n {self.my_store_full}')
                return f'Выход'
            else:
                return StoreMashines.reception(self)


    class Printer(StoreMashines):
        def to_print(self):
            return f'to print smth {self.numb} times'


    class Scanner(StoreMashines):
        def to_scan(self):
            return f'to scan smth {self.numb} times'


    class Copier(StoreMashines):
        def to_copier(self):
            return f'to copier smth  {self.numb} times'


    unit_1 = Printer('hp', 2000, 5, 10)
    unit_2 = Scanner('Canon', 1200, 5, 10)
    unit_3 = Copier('Xerox', 1500, 1, 15)
    print(unit_1.reception())
    print(unit_2.reception())
    print(unit_3.reception())
    print(unit_1.to_print())
    print(unit_3.to_copier())

else:
    pass

print('Доделать! ***')

# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
print("Урок 8. Задание 7.")

part7 = input('Выполнить задание 7? (Y/N)')
if part7.title() == 'Y':

    class ComplexNumber:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __add__(self, other):
            za = self.a + other.a
            zb = self.b + other.b
            print(f'Сумма z1 и z2 равна:')
            if zb >= 0:
                return f'= {za} + {zb}i'
            else:
                return f'= {za} - {-1 * zb}i'

        def __mul__(self, other):
            za = self.a * other.a - (self.b * other.b)
            zb =  self.a*other.b + self.b * other.a
            print(f'Произведение z1 и z2 равно:')
            if zb >= 0:
                return f'= {za} + {zb}i'
            else:
                return f'= {za} - {-1 * zb}i'

        def __str__(self):
            if self.b >= 0:
                return f'= {self.a} + {self.b}i'
            else:
                return f'= {self.a} - {-1 * self.b}i'


    z_1 = ComplexNumber(int(input('Введите вещественную часть комплексного числа z1, a: ')), int(input('Введите мнимую часть комплексного числа z1, b: ')))
    z_2 = ComplexNumber(int(input('Введите вещественную часть комплексного числа z2, a: ')), int(input('Введите мнимую часть комплексного числа z1, b: ')))
    print('z\u2081', z_1)
    print('z\u2082', z_2)
    print('z\u2081\u208a\u2082', z_1 + z_2)
    print('z\u2081\u2093\u2082', z_1 * z_2)

else:
    pass

print('Задание выполнено!')