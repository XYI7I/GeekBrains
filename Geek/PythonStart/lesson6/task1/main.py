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
str_equation = '2+(1+(2*3))/(4-10)'

# print(str_equation[str_equation.rindex('(') + 1:][:str_equation[str_equation.rindex('(') + 1:].index(')')])
print(str_equation[:str_equation.rindex('(')])
str_equation1 = str_equation[str_equation.rindex('('):]
print(str_equation[str_equation.rindex('('):])
print(str_equation[str_equation.rindex('('):][:str_equation[str_equation.rindex('('):].index(')')+1])


print(eval('2+(1+(2*3))/(4-10)'))


def find_res_from_str(str_equation):
    """
    """
    global result_eq
    list_opr = ['+', '-', '*', '/']
    list_var = []
    str_var = ''
    # print(eval(str_equation))
    count_op = str_equation.count('(')
    count_cl = str_equation.count(')')

    if count_op == count_cl == 0:
        for el in str_equation:
            if el not in list_opr:
                str_var += el
            else:
                list_var.append(int(str_var))
                str_var = ''
                list_var.append(el)
        list_var.append(int(str_var))
        result_eq = make_arif_solution(list_var)


    elif count_op != count_cl:
        print(str_equation)
        print('Error!')
        exit()

    else:
        print(str_equation[str_equation.rindex('(') + 1:][:str_equation[str_equation.rindex('(') + 1:].index(')')])
        result_str = str(find_res_from_str(str_equation[str_equation.rindex('(') + 1:][:str_equation[str_equation.rindex('(') + 1:].index(')')]))
        str_equation_temp = str_equation[:str_equation.rindex('(')] + result_str + str_equation[str_equation.rindex('('):][str_equation[str_equation.rindex('('):].index(')')+1:]
        print(str_equation_temp)
        find_res_from_str(str_equation_temp)

    return result_eq


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

    # print(list_var)

    return result_equ


result = find_res_from_str('2+(1+(2*3))/(4-10)')
print(result)
