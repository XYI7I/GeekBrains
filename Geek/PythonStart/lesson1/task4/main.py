"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""
def findRangeXY(numQ):
    result_str = 'X > 0 и Y < 0'
    if numQ == 1:
        result_str = 'X > 0 и Y > 0'
    elif numQ == 2:
        result_str = 'X < 0 и Y > 0'
    elif numQ == 3:
        result_str = 'X < 0 и Y < 0'

    print(f"Диапазон возможных координат находится в следющих интервалах: {result_str}")

numQ = 0

while numQ < 1 or numQ > 4:
    numQ = int(input('Введите номер четверти Q (1-4): '))

findRangeXY(numQ)