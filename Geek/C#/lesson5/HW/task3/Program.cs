// 38.  Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.
Console.WriteLine("Программа показывает сумму максимального и минимального элемента в масиве.");

int[] GenArray()
{
    Console.Write("Введите число элементов массива: ");
    int n = int.Parse(Console.ReadLine ());
    int[] arr = new int[n];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(-100, 101);
    }
    return arr;
}

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}

int SumMinMaxArray(int[] arr)
{
    int minarr = arr[0];
    int maxarr = arr[0];
    int sum = 0;
    for (int i = 1; i < arr.Length; i++)
    {
        if (arr[i] < minarr)
        {
            minarr = arr[i];
        }
        else if (arr[i] > maxarr)
        {
            maxarr = arr[i];
        }
    }
    
    sum = minarr + maxarr;
    return sum;
}

int MinArray(int[] arr)
{
    int minarr = arr[0];

    for (int i = 1; i < arr.Length; i++)
    {
        if (arr[i] < minarr)
        {
            minarr = arr[i];
        }
    }
    
    return minarr;
}

int MaxArray(int[] arr)
{
    int maxarr = arr[0];
    
    for (int i = 1; i < arr.Length; i++)
    {
        if (arr[i] > maxarr)
        {
            maxarr = arr[i];
        }
    }
    
    return maxarr;
}


int[] newarr = GenArray();
PrintArray(newarr);
//int summinmax = SumMinMaxArray(newarr);
int mina = MinArray(newarr);
int maxa = MaxArray(newarr);
//Console.WriteLine($"Сумма максимального {maxa} и минимального {mina} элемента в масиве -> {summinmax}");
Console.WriteLine($"Сумма максимального {maxa} и минимального {mina} элемента в масиве -> {maxa + mina}");