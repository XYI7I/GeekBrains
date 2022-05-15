// Программа по сортировке одномерного массива:
Console.WriteLine("Программа по сортировке одномерного массива");

int[] arr = {1, 5, 4, 10, 8, 18, 21, 102, 3, 4, 56, 78};

void PrintArray(int[] array)
{
    int count = array.Length;

    for (int i = 0; i < count; i++)
    {
        Console.WriteLine($"{array[i]} ");
    }
    Console.WriteLine();
}

void SelectionSort(int[] array)
{
    for (int i = 0; i < array.Length - 1; i++)
    {
        int minPosition = i;
        for (int j = i + 1; j < array.Length; j++)
        {
            if (array[j] < array[minPosition]) minPosition = j;
        }
        int temparray = array[i];
        array[i] = array[minPosition];
        array[minPosition] = temparray;
    }
}


var str = string.Join(" ", arr);
Console.WriteLine(str);;

SelectionSort(arr);

var str1 = string.Join(" ", arr);
Console.WriteLine(str1);