"""
Реализуйте алгоритм перемешивания списка.
"""
from random import randint, shuffle, sample

def makeListNumNelem(N):
    listNum =[]
    for i in range(N):
        listNum.append(randint(-1 * N, N))
    return listNum

def shuffleList(list):
    newlist = []
    countlist = []
    while len(countlist) != len(list):
        pos = randint(0, len(list) - 1)
        if pos not in countlist:
            countlist.append(pos)
            newlist.append(list[pos])
    return newlist

list1 = makeListNumNelem(10)

list2 = list1.copy()
shuffle(list2)

print(list1)
print(list2)

list3 = shuffleList(list1)
print(list3)