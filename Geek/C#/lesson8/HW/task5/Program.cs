// 62. Заполните спирально массив 4 на 4.
Console.WriteLine("Программа заполнит спиралыьно массив 4 на 4.");

int[,] SpiralArray4x4()
{
    int[,] arr = new int[4, 4];
    int k = 1;  

    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
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

int[,] arr = SpiralArray4x4();
PrintArray(arr);


    0.0
    0.1
    0.2
    0.3
    1.3
    2.3
    3.3
    3.2
    3.1
    3.0
    2.0
    1.0
    1.1
    1.2
    2.2
    2.1