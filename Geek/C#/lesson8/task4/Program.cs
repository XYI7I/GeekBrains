// 59. Задайте двумерный массив из целых чисел. Напишите программу, которая удалит строку и столбец, на пересечении которых расположен наименьший элемент массива.
Console.WriteLine("Программа удалит строку и столбец, на пересечении которых расположен наименьший элемент массива.");

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


void RemoveRowColumnMinList(int[,] arr)
{
    int[,] newarr = new int[arr.GetLength(0) - 1, arr.GetLength(1) - 1];
    
    int min = arr[0,0];
    int imin = 0;
    int jmin = 0;
    
    for (int i = 0; i < arr.GetLength(0); i++)
        for (int j = 0; j < arr.GetLength(1); j++)
            if (arr[i,j] < min)
            {
                min = arr[i,j];
                imin = i;
                jmin = j;
            }
    
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        if (i != imin)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                if(j != jmin)
                    Console.Write(arr[i,j] + " ");
            }
            Console.WriteLine();            
        }
    }
    
}

int[,] RemoveRCMinList(int[,] arr)
{
    int[,] newarr = new int[arr.GetLength(0) - 1, arr.GetLength(1) - 1];
    
    int min = arr[0,0];
    int imin = 0;
    int jmin = 0;
    
    for (int i = 0; i < arr.GetLength(0); i++)
        for (int j = 0; j < arr.GetLength(1); j++)
            if (arr[i,j] < min)
            {
                min = arr[i,j];
                imin = i;
                jmin = j;
            }
    
    int flagI = 0;
    int flagJ = 0;
    for (int i = 0; i < newarr.GetLength(0); i++)
    {
        {
            for (int j = 0; j < newarr.GetLength(1); j++)
            {
                if (i >= imin) flagI = 1;
                else flagI = 0;
                if (j >= jmin) flagJ = 1;
                else flagJ = 0;
                
                newarr[i,j] = arr[i + flagI, j + flagJ];
            }
        }
    }
    return newarr;
    
}

int[,] array = GenArray();
PrintArray(array);
Console.WriteLine();
RemoveRowColumnMinList(array);
int[,] newarray = RemoveRCMinList(array);
PrintArray(newarray);