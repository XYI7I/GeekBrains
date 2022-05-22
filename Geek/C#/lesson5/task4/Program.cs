// 35. Задайте одномерный массив из 123 случайных чисел. Найдите количество элементов массива, значения которых лежат в отрезке [10,99].
Console.WriteLine("Программа найдет количество элементов массива, значения которых лежат в отрезке [10,99]");

int[] GenArray()
{
    //Console.Write("Введите число элементов массива: ");
    //int n = int.Parse(Console.ReadLine ());
    int[] arr = new int[123];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(100);
    }
    return arr;
}

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}

int FindCountNumArr(int[] arr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] < 100 && arr[i] > 9)
        {
            count++;
        }
    }
    return count;
}

int[] newarr = GenArray();
PrintArray(newarr);
int counint = FindCountNumArr(newarr);
Console.WriteLine($"Количество элементов массива, значения которых лежат в отрезке [10,99] -> {counint}");