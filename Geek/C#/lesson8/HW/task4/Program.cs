// 60. Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
Console.WriteLine("Программа будет построчно выводить трехмерный массив, добавляя индексы каждого элемента.");

int[,,] Gen3DArray()
{
    Console.Write("Введите число строк массива m: ");
    int m = int.Parse(Console.ReadLine ());
    Console.Write("Введите число столбцов массива n: ");
    int n = int.Parse(Console.ReadLine ());
    Console.Write("Введите число столбцов массива n: ");
    int l = int.Parse(Console.ReadLine ());
    int[,,] arr = new int[m, n, l];
    int num = 0;
    Random rand = new Random();
    int[] listnum = new int[m * n * l];   
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < l; k++)
            {
                num = rand.Next(10, 100);
                
                while (Array.IndexOf(listnum, num) != -1)
                {
                    num = rand.Next(9, 100);
                }
                listnum[i*n*l+j*n+k] = num;
                    

                arr[i, j, k] = num;
            }
    // Для проверки на уникальность элементов
    //int[] sortArr = listnum.Distinct().ToArray();
    
    //var str = string.Join(" ", sortArr);
    //Console.WriteLine(str);
    //Console.WriteLine(sortArr.Length);
    //Array.Sort(sortArr);

    //var str1 = string.Join(" ", sortArr);
    //Console.WriteLine(str1);

    return arr;
}

void Print3DArray(int[,,] prarr)
{
    for (int i = 0; i < prarr.GetLength(0); i++)
    { 
        for (int j = 0; j < prarr.GetLength(1); j++)
        { 
            for (int k = 0; k < prarr.GetLength(2); k++)
                    Console.Write($"{prarr[i,j,k]}({i}, {j}, {k}); ");
            Console.WriteLine();
        }
        Console.WriteLine();
    }
}

int[,,] arr3d = Gen3DArray();
Print3DArray(arr3d);