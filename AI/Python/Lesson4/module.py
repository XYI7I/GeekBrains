from random import randint

def gen_randint_list(N):
    new_list = []

    for el in range(N):
        el = randint(1, N)
        new_list.append(el)

    return new_list

def compare(list):
    new_list = []
    for el in range(1, len(list)):
        if list[el] > list[el - 1]:
            new_list.append(list[el])
    return new_list