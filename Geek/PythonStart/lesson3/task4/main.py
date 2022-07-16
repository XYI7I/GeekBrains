"""
 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

 Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
 """


def dec_to_bin(num):
    """
    Функция преобразовывает десятичное число в двоичное.

    Пример:
    - 45 -> 101101

    :param num: int
    """
    num_bin = ''
    if num == 0:
        num_bin = '0'
    while num != 0:
        num_bin = str(num % 2) + num_bin
        num //= 2

    print(num_bin)


dec_to_bin(45)
dec_to_bin(3)
dec_to_bin(2)
