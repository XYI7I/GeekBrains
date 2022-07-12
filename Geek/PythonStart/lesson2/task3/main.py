"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:

- Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""
def makeListSubseq(N):
    listNum =[]
    sum = 0
    for i in range(1, N + 1):
        num = (1 + 1 / i) ** i
        sum += num
        listNum.append(round(num, 4))
    return listNum, sum

listSubseq, SubseqSum = makeListSubseq(3)
print(f'Сумма элементов последовательности {listSubseq} = {round(SubseqSum, 4)}')