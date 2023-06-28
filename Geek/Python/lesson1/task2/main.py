"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""
def inputNumbers():
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(3):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(arr):
    left = not (arr[0] or arr[1] or arr[2])
    right = not arr[0] and not arr[1] and not arr[2]
    result = left == right
    return result


statement = inputNumbers()

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
