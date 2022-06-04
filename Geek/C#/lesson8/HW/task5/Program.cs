// 62. Заполните спирально массив 4 на 4.
Console.WriteLine("Программа заполнит спиралыьно массив 4 на 4.");

int[,] SpiralArray4x4()
{
    int[,] arr = new int[4, 4];
  

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            arr[i, j] = k++;
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
