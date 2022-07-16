"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его

Пример:

- 6782 -> 23
- 0,56 -> 11

"""


def find_sum_dig_of_num():
    """
    Функция находит сумму цифр заданного числа.
    """
    num = input('Input number: ')
    SumDig = 0
    for el in range(len(num)):
        try:
            SumDig += int(num[el])
        except:
            pass
    return num, SumDig


num, sum_dig = find_sum_dig_of_num()
print(f'Сумма цифр в числе {num} = {sum_dig}')
