# coding: utf-8

# Основы языка Python.
# Занятие 7. Объектно-ориентированное программирование. Продвинутый уровень

# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
print("Урок 7. Задание 1.")


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2
        self.init_matrix = [[0 for j in range(len(self.list_1[0]))] for i in range(len(self.list_1))]

    def __add__(self):
        if len(self.list_1) == len(self.list_2) and len(self.list_1[0]) == len(self.list_2[0]):
            for i in range(len(self.list_1)):

                for j in range(len(self.list_2[0])):
                    self.init_matrix[i][j] = (self.list_1[i][j] + self.list_2[i][j])
        else:
            print('error')

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.init_matrix]) + '\n')

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]) + '\n\n' + '\n'.join(
            ['\t'.join([str(j) for j in i]) for i in self.list_2]))


my_matrix = Matrix([[1, 2, 3],
                    [5, 8, 13],
                    [21, 34, 45],
                    [21, 34, 45]],
                   [[45, 34, 21],
                    [13, 8, 5],
                    [3, 2, 1],
                    [21, 34, 45]])

print(my_matrix.__add__())
print(my_matrix.__str__())

print('***')

# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У
# этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 +
# 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.
print("Урок 7. Задание 2.")


class Clothes:
    def __init__(self, V_size, H_size):
        self.V_size = V_size
        self.H_size = H_size

    def get_square_coat(self):
        return self.V_size / 6.5 + 0.5

    def get_square_suit(self):
        return self.H_size * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'Суммарный расход ткани на производство одежды \n'
                   f' {(self.V_size / 6.5 + 0.5) + (self.H_size * 2 + 0.3):.2g} м\u00b2')


class Coat(Clothes):
    def __init__(self, V_size, H_size):
        super().__init__(V_size, H_size)
        self.square_coat = self.V_size / 6.5 + 0.5

    def __str__(self):
        return f'Расход ткани на производство пальто {self.square_coat:.2g} м\u00b2'


class Suit(Clothes):
    def __init__(self, V_size, H_size):
        super().__init__(V_size, H_size)
        self.square_suit = self.H_size * 2 + 0.3

    def __str__(self):
        return f'Расход ткани на производство костюма {self.square_suit:.2g} м\u00b2'


coat = Coat(2, 0)
suit = Suit(0, 2)
print(coat)
print(suit)
# print(get_sq_full)
# print(suit.get_sq_full)
# print(suit.get_square_coat())
# print(suit.get_square_suit())

print('***')

# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа. Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно
# равняться сумме ячеек исходных двух клеток. Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
# если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение. Умножение.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух
# клеток. Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток. В классе необходимо реализовать метод make_order(), принимающий экземпляр класса
# и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида
# *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда
# не хватает, то в последний ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**. Или, количество ячеек клетки
# равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
print("Урок 7. Задание 3.")


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        '''
        Выдает ошибку о том, что результат не число  при вычислении
        if int(Cell(self.quantity - other.quantity)) > 0:
            return Cell(int(self.quantity - other.quantity))
        else:
            return f'Операция вычитания невозможна'""
        '''
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Отрицательно!')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(10)
cells2 = Cell(2)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)

print('Задание выполнено!')
