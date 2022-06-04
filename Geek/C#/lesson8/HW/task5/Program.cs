// 62. Заполните спирально массив 4 на 4.
Console.WriteLine("Программа заполнит спиралыьно массив N x N.");

int[,] SpiralArrayNxN()
{
    Console.Write("Введите размер массива NxN, N: ");
    int n = int.Parse(Console.ReadLine ());
    //int n = 4;
    int[,] arr = new int[n, n];
    int k = 1;
    int itr = n/2 + n%2;

    for (int i = 0; i < itr; i++)
    {
        for (int j = i; j < n - i; j++)
        {
            arr[i,j] = k++;
            if (k == n * n)
                return arr;
        }            
        for (int j = i + 1; j < n-i; j++)
            arr[j,n - i - 1] = k++;
        for (int j = n - i - 2; j >= i; j--)
        {
            arr[n - i - 1,j] = k++;
            if (k == n * n)
                return arr;
        }
        for (int j = n - i - 2; j >= i + 1; j--)
            arr[j,i] = k++;

    }
    return arr;
}

void PrintArray(int[,] prarr)
{
    for (int i = 0; i < prarr.GetLength(0); i++)
    {
        for (int j = 0; j < prarr.GetLength(1); j++)
        {
            Console.Write(prarr[i,j] + "\t");
        }
        Console.WriteLine();
    }
}

int[,] arr = SpiralArrayNxN();
PrintArray(arr);