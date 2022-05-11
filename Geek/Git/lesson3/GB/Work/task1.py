# Задача №1. Написать программу для копирования массива.
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
                        self.mult_array[k] += (self.list[i] * other.list[j])

        return Array(self.mult_array)


array1 = Array([1, 2, 3])

array2 = Array([45, 34])

print(array1)
print(array2)
print(array2 * array1)