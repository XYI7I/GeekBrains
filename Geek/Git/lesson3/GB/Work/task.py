# Задача №1. Написать программу для копирования массива.

# Задача №2 с элементами математики.
# Написать программу для операции "произведение массивов". Сама операция определяется так, как будто элементы массива
# - это коэффициенты полинома. Соответственно, произведение массивов - должно дать новый массив, коэффициенты которого
# соответсвуют нужному полиному. Например, возьмем полином (x - 1) и полином (x + 2). Их можно представить в виде
# массивов [-1, 1] и [2, 1] соответственно. Индекс элемента в массиве соответствует степени x при этом коээфициенте,
# т.е. полином (x - 1) можно переписать как (-1 * x0 + 1 * x1 ), таким образом соответсвующий этому полиному массив
# будет иметь вид [-1, 1]. По указанному правилу произведение массивов [-1, 1] и [2, 1] должно быть равно [-2, 1, 1],
# т.к. (x - 1) * (x + 2) = ( x2 + x1 - 2).

class Array:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        return str('\t'.join([str(i) for i in self.list]) + '\n')

    # def __copy__(self):

    def __mul__(self, other):
        self.mult_array = [0 for i in range(len(self.list) + len(other.list) - 1)]
        for k in range(len(self.mult_array)):
            for i in range(len(self.list)):
                for j in range(len(other.list)):
                    if i + j == k:
                        self.mult_array[k] += self.list[i] * other.list[j]

        return Array(self.mult_array)

    def __copy__(self):
        self.copy_array = [0 for i in range(len(self.list))]
        for i in range(len(self.copy_array)):
            self.copy_array[i] = self.list[i]

        return Array(self.copy_array)


from copy import copy

array1 = Array([1, 2, 3])
array2 = Array([45, 34])
copy_array = copy(array1)

print(array1)
print(array2)

# Задача №1
print('Задача №1\n')
print(copy_array)


# Задача №2
print('Задача №2\n')
print(array2 * array1)
print(array1 * array2)
