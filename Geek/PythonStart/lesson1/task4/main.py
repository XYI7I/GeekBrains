"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""
numQ = 0

while numQ < 1 or numQ > 4:
    numQ = int(input('Введите номер четверти Q (1-4): '))

if numQ == 1:
    print('X > 0; Y > 0')
elif numQ == 2:
    print('X < 0; Y > 0')
elif numQ == 3:
    print('X < 0; Y < 0')
else:
    print('X > 0; Y < 0')