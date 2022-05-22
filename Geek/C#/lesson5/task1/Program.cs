// 31. Задайте массив из 12 элементов, заполненный случайными числами из промежутка [-9, 9]. Найдите сумму отрицательных и положительных элементов массива.
Console.WriteLine("Задайте массив из 12 элементов, заполненный случайными числами из промежутка [-9, 9]. Найдите сумму отрицательных и положительных элементов массива.");

int[] GenArray()
{
    //Console.Write("Введите число элементов массива: ");
    //int N = int.Parse(Console.ReadLine ());
    int[] arr = new int[20];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(-9, 10);
    }
    return arr;
}

void SumArr(int[] arrw)
{
    int plus = 0;
    int neg = 0;

    for (int i = 0; i < arrw.Length; i++)
    {
        if (arrw[i] >= 0)
        {
            plus += arrw[i];
        }

        else
        {
            neg += arrw[i];
        }

    }
    Console.WriteLine(plus);
    Console.WriteLine(neg);
    
}

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}

int[] newarr = GenArray();
PrintArray(newarr);
SumArr(newarr);