// Доп. задание*. Задать целочисленный двумерный массив размерности m х n. Выяснить, в какой строке последовательность является возрастающей или убывающей.
Console.WriteLine("Программа создает двумерный целочисленный массив размером m x n, и определяет в какой строке последовательность является возрастающей или убывающей.");

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
            arr[i, j] = rand.Next(-10, 11);
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
            Console.Write(prarr[i,j] + "\t");
        }
        Console.WriteLine();
    }
}

void IncreasesDecreaseRowArray(int[,] arr)
{
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        int coef = 0;
        for (int j = 1; j < arr.GetLength(1); j++)
        {
            if (arr[i, j-1] < arr[i, j])
                coef++;
            if (arr[i, j] < arr[i, j-1])
                coef--;
        }
        if (Math.Abs(coef) == arr.GetLength(1) - 1)
        {
            string res =  coef > 0 ? $"Последовательность в строке - {i} является возрастающей." : $"Последовательность в строке - {i} является убывающей.";
            Console.WriteLine(res);
        }
    }
}

int[,] array = GenArray();
PrintArray(array);
Console.WriteLine();
IncreasesDecreaseRowArray(array);