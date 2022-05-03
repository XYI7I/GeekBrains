from random import randint

def gen_randint_list(N):
    '''
    Generator of random integer list.
    :param N: - element's quantity
    :return: - random integer list
    '''
    new_list = []

    for el in range(N):
        el = randint(1, N)
        new_list.append(el)

    return new_list

def compare(list):
    '''
    Compare neighboring list's elements if element[i] > element[i-1].
    :param list: element's list
    :return: new list with elements from list which element[i] > element[i-1]
    '''
    new_list = []
    
    for el in range(1, len(list)):
        if list[el] > list[el - 1]:
            new_list.append(list[el])
    return new_list