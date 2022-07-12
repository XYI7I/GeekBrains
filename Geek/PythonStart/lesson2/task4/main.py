"""
 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
 """
from random import randint

def makeListNumNelem(N):
    listNum =[]
    for i in range(N):
        listNum.append(randint(-1 * N, N))
    return listNum

def findMultListElPosition(list):
    file = open('file.txt', 'r')
    Lines = file.readlines()
    mult = 1
    for line in Lines:
        mult *= list[int(line)]
    return mult

list1 = makeListNumNelem(10)
print(list1)

multlistel = findMultListElPosition(list1)
print(f'произведение элементов на указанных позициях (file.txt) = {multlistel}')