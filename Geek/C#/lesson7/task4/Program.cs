// 51. Задайте двумерный массив. Найдите сумму элементов главной диагоналиэлементы.
Console.WriteLine("Найдем сумму элементов главной диагонали массива.");

int[,] GenArray()
{
    Console.Write("Введите число строк массива m: ");
    int m = int.Parse(Console.ReadLine ());
    Console.Write("Введите число строк массива n: ");
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

int SumElemDiagArray(int[,] arr)
{   
    int n = 0;
    if (arr.GetLength(0) < arr.GetLength(1))
        n = arr.GetLength(0);
    else n = arr.GetLength(1);
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += arr[i,i];
    }
    return sum;
}

int[,] array = GenArray();
PrintArray(array);
Console.WriteLine();
int sum = SumElemDiagArray(array);
Console.WriteLine(sum);
