// 53. Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.
Console.WriteLine("Программа поменяет местами первую и последнюю строку массива.");

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
            arr[i, j] = rand.Next(11);
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

int[,] ChangeRowArray(int[,] arr)
{
    int temp = 0;
    for (int i = 0; i < arr.GetLength(1); i++)
    {
        temp = arr[0, i];
        arr[0, i] = arr[arr.GetLength(0) - 1, i];
        arr[arr.GetLength(0) - 1, i] = temp;    
    }
    return arr;
}




int[,] array = GenArray();
PrintArray(array);
Console.WriteLine();
int[,] newarr = ChangeRowArray(array);
PrintArray(newarr);