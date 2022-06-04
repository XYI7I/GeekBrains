// 57. Составить частотный словарь элементов двумерного массива. Частотный словарь содержит информацию о том, сколько раз встречается элемент входных данных.
Console.WriteLine("Программа создает частотный словарь. Частотный словарь содержит информацию о том, сколько раз встречается элемент входных данных.");

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


void FrequencyList(int[,] arr)
{
    int[] listar = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int count = 0;
    for (int k = 0; k < listar.Length; k++)
    {
        for (int i = 0; i < arr.GetLength(0); i++)
            {
                for (int j = 0; j < arr.GetLength(1); j++)
                {
                    if (listar[k] == arr[i,j])
                    count++;
                }

            }
        if (count != 0)
        {
            Console.WriteLine($"{listar[k]} встречаеться {count} раз");
        }
        count = 0;
    }

        
}

int[] OneDimArray(int[,] arr)
{
    int [] newarr = new int[arr.GetLength(0) * arr.GetLength(1)];
    for (int i = 0; i < arr.GetLength(0); i++)
        for (int j = 0; j < arr.GetLength(1); j++)
            newarr[i + j] = arr[i,j];
    return newarr;
}

int[,] array = GenArray();
PrintArray(array);
Console.WriteLine();

int[] newarray = OneDimArray(array);
PrintArray(newarray);

Console.WriteLine();

FrequencyList(array);
