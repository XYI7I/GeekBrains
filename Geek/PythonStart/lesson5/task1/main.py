"""
В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


"""

def find_lose_num(file_name):
    """
    Функция находит пропущеное число в списке условие A[i] - 1 = A[i-1].
    """
    file = open(file_name, 'r')
    numbers = file.read().split()
    for i in range(0, len(numbers) - 1) :
        if int(numbers[i + 1]) - int(numbers[i]) != 1:
            fnum = int(numbers[i]) + 1
        i += 1
    return fnum


fnum = find_lose_num('number.txt')
print(fnum)
