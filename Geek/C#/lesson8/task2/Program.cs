// 55. Задайте двумерный массив. Напишите программу, которая заменяет строки на столбцы. В случае, если это невозможно, программа должна вывести сообщение для пользователя.
Console.WriteLine("Программа заменяет строки на столбцы. В случае, если это невозможно, программа должна вывести сообщение для пользователя.");

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

int[,] ChangeRowColumnArray(int[,] arr)
{
        
    int[,] newarr = new int[arr.GetLength(1), arr.GetLength(0)];
    for (int i = 0; i < arr.GetLength(1); i++)
    {
        for(int j = 0; j < arr.GetLength(0); j++)
        {
            newarr[i, j] = arr[j, i];
        }
    }
    return newarr;
}




int[,] array = GenArray();
PrintArray(array);
Console.WriteLine();
int[,] newarr = ChangeRowColumnArray(array);
PrintArray(newarr);
