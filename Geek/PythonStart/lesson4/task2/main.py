"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

"""


def find_list_simpl_div(n):
    """
    Функция составит список простых множителей числа N
    """
    simpl_num_list(n)
    file = open('simp_num.txt', 'r')
    div_simp = file.read().split()
    file.close()
    for el in div_simp:
        if n % int(el) == 0:
            print(el)



def simpl_num_list(num):
    """
    Определение простое число или нет
    """
    file = open('simp_num.txt', 'r')
    simp_numbers = file.read().split()
    file.close()
    last_el = int(simp_numbers[len(simp_numbers) - 1])
    if num > last_el:
        for i in range(last_el + 1, abs(num) + 1):
            sim_num = find_simpl_num(i)
            if sim_num is not None:
                file = open('simp_num.txt', 'a')
                file.write(" " + str(sim_num))
                file.close()


def find_simpl_num(num):
    """Определение простое число или нет"""
    for i in range(2, abs(num)):
        if num % i == 0:
            return
    return num

find_list_simpl_div(21)