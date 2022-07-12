"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его

Пример:

- 6782 -> 23
- 0,56 -> 11

"""
def findSumDigofNum():
    num = input('Input number: ')
    SumDig = 0
    for el in range(len(num)):
        try:
            SumDig += int(num[el])
        except:
            pass
    return num, SumDig

num, sumdig = findSumDigofNum()
print(f'Сумма цифр в числе {num} = {sumdig}')
