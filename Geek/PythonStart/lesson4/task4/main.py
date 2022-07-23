"""
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""

def create_polyvalent_k(k):
    """
    Функция создает многочелен степени k и записывает его в фаил
    значения коэффициентов случайны от 0 до 100)

    Пример:
    - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
    """
    from random import randint
    file = open('polyvalent', 'a+')
    koeff_list = []
    for i in range(0, k + 1):
        koeff = str(randint(0, 100))
        file.write(koeff + ' ')

    file.write('\n')
    file.close()



create_polyvalent_k(2)