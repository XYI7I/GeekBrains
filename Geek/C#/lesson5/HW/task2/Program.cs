// 36.  Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.
Console.WriteLine("Программа показывает сумму элементов в масиве стоящщих на четных местах.");

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

int SumEvenIndArray(int[] arr)
{
    int sum = 0;
    for (int i = 0; i < arr.Length; i = i + 2)
    {
        sum = sum + arr[i];
    }
    return sum;
}

int[] newarr = GenArray();
PrintArray(newarr);
int sumevin = SumEvenIndArray(newarr);
Console.WriteLine($"Сумма элементов в масиве стоящщих на четных местах -> {sumevin}");