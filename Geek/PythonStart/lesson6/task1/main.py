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
b = '(1+(2*3)/4)-10'
print(b[b.rindex('(')+1:b.index(')')])

def find_res_from_str(str_equation):
    """
    """
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
    # print(eval(str_equation))
    count_op = str_equation.count('(')
    count_cl = str_equation.count(')')
    while count_op != 0:

        result = make_arif_solution(list_var)
        return result


def make_arif_solution(list_var):
    """
    """
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


# result = find_res_from_str('1+2*3/4-10')
# print(result)
