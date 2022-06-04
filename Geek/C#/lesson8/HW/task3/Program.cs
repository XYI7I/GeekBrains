// 58. Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
Console.WriteLine("Программа находит произведение двух матриц.");

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

int[,] MultArray(int[,] arr1, int[,] arr2)
{
    if (arr1.GetLength(1) != arr2.GetLength(0))
    {
        Console.WriteLine("Не возможно перемножение несовместных матриц!");
        return null;
    }
    int[,] multarr = new int[arr1.GetLength(0), arr2.GetLength(1)];
    for (int i = 0; i < multarr.GetLength(0); i++)
        for (int j = 0; j < multarr.GetLength(1); j++)
            for (int k = 0; k < arr1.GetLength(1); k++)
                multarr[i,j] += arr1[i,k] * arr2[k,j];

    return multarr;
}

int[,] arr1 = GenArray();
PrintArray(arr1);
Console.WriteLine();
int[,] arr2 = GenArray();
PrintArray(arr2);
Console.WriteLine();

int[,] multarr = MultArray(arr1, arr2);
PrintArray(multarr);