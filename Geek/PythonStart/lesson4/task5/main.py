"""
Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
"""


def create_sum_polyvalent():
    """
    Функция создает многочелен степени k и записывает его в фаил
    значения коэффициентов случайны от 0 до 100)

    Пример:
    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
    """
    print('+')


def array_from_file(name):
    koeff_arr = []
    file = open(name, 'r')
    lines = file.readlines()
    for line in lines:
        koeff_arr.append(line.split(' '))
        file.close()

    return koeff_arra


