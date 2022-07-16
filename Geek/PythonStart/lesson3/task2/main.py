"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]

def find_mul_pair_pos(list_num):
    """
    Функция находит произведение элементов произведение пар чисел списка

    Пример:
    - [2, 3, 4, 5, 6] => [12, 15, 16];
    - [2, 3, 5, 6] => [12, 15]
    """
    mul_list = []
    for i in range(len(list_num)//2 + len(list_num) % 2):
        mul_list.append(list_num[i] * list_num[len(list_num) - i - 1])
    return mul_list


find_mult1 = find_mul_pair_pos(list1)
find_mult2 = find_mul_pair_pos(list2)

print(f' Произведение пар чисел списка {list1} = {find_mult1}')
print(f' Произведение пар чисел списка {list2} = {find_mult2}')



