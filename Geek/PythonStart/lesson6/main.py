"""
1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

    *Пример:*

    2+2 => 4;

    1+2*3 => 7;

    1-2*3 => -5;

- Добавьте возможность использования скобок, меняющих приоритет операций.

        *Пример:*

        1+2*3
         => 7;

        (1+2)*3 => 9;

"""


def find_res_from_str(str_equation):
    list_opr = ['+', '-', '*', '/']
    list_var = []
    str_var = ''
    for el in str_equation:
        if el not in list_opr:
            str_var += el
        else:
            list_var.append(int(str_var))
            str_var = ''
            list_var.append(el)
    list_var.append(int(str_var))
    print(eval(str_equation))
    result = make_arif_solution(list_var)
    return result


def make_arif_solution(list_var):
    i = 0
    result_equ = 0

    while ('*' in list_var) or ('/' in list_var):

        if list_var[i] == '*':
            result_equ += list_var[i - 1] * list_var[i + 1]
            list_var[i + 1] = result_equ
            del list_var[i - 1: i + 1]
            i = 0
            result_equ = 0

        elif list_var[i] == '/':
            result_equ += list_var[i - 1] / list_var[i + 1]
            list_var[i + 1] = result_equ
            del list_var[i - 1: i + 1]
            i = 0
            result_equ = 0
        else:
            i += 1
    print(list_var)

    while ('+' in list_var) or ('-' in list_var):

        if list_var[i] == '+':
            result_equ += list_var[i - 1] + list_var[i + 1]
            list_var[i + 1] = result_equ
            del list_var[i - 1: i + 1]
            i = 0
            result_equ = 0

        elif list_var[i] == '-':
            result_equ += list_var[i - 1] - list_var[i + 1]
            list_var[i + 1] = result_equ
            del list_var[i - 1: i + 1]
            i = 0
            result_equ = 0
        else:
            i += 1

    result_equ = list_var[0]

    print(list_var)

    return result_equ


result = find_res_from_str('1+2*3/4-10')
print(result)

'''
Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

*Пример:* 

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

'''


def find_uniq_el(list):
    max_elem = max(list) + 1
    count = [0] * max_elem

    for element in list:
        count[element] += 1

    result = []
    for element in list:
        if count[element] == 1:
            result.append(element)
    return result


list_num = [1, 2, 3, 5, 1, 5, 3, 10]
print(list_num)
list_unq = find_uniq_el(list_num)
print(list_unq)

"""
import re

actions = {
    "^": lambda x, y: str(float(x) ** float(y)),
    "*": lambda x, y: str(float(x) * float(y)),
    "/": lambda x, y: str(float(x) / float(y)),
    "+": lambda x, y: str(float(x) + float(y)),
    "-": lambda x, y: str(float(x) - float(y))
}

priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"


def my_eval(expresion: str) -> str:
    while (match := re.search(priority_reg_exp, expresion)):
        expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))

    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion: str = expresion.replace(match.group(0), action(*match.groups()))

    return expresion

exp = "".join(input('Введите строковое выражение: ').split())
print(my_eval(exp), eval(exp))

"""
