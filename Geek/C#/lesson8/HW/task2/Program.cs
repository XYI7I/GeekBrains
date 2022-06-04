// 56. Задайте прямоугольный двумерный массив. Напишите программу, которая будет находить строку с наименьшей суммой элементов.
Console.WriteLine("Программа находит строку с наименьшей суммой элементов.");

int[,] GenArray()
{
    Console.Write("Введите число строк массива m: ");
    int m = int.Parse(Console.ReadLine ());
    Console.Write("Введите число столбцов массива n: ");
    int n = int.Parse(Console.ReadLine ());
    int[,] arr = new int[m, n];
    Random rand = new Random();

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            arr[i, j] = rand.Next(10);
        }

    }
    return arr;
}

void PrintArray(int[,] prarr)
{
    for (int i = 0; i < prarr.GetLength(0); i++)
    {
        for (int j = 0; j < prarr.GetLength(1); j++)
        {
            Console.Write(prarr[i,j] + " ");
        }
        Console.WriteLine();
    }
}

void MinSumRowArray(int[,] arr)
{
    int minrow = 0;
    int[] sumarr = new int[arr.GetLength(0)];
            
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
            sumarr[i] += arr[i, j];
    }
    minrow = Array.IndexOf(sumarr, sumarr.Min());
    Console.WriteLine($"Cтрокa с наименьшей суммой элементов = {sumarr.Min()} --> строка {minrow + 1}.");
}

int[,] arr = GenArray();
PrintArray(arr);
Console.WriteLine();
MinSumRowArray(arr);