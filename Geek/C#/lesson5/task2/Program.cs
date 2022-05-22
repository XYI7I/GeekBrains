// 32. Напишите программу замена элементов массива: положительные элементы замените на соответствующие отрицательные, и наоборот.
Console.WriteLine("Программа меняет элементы массива: положительные элементы на отрицательные, и наоборот.");

int[] GenArray()
{
    Console.Write("Введите число элементов массива: ");
    int n = int.Parse(Console.ReadLine ());
    int[] arr = new int[n];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(-99, 100);
    }
    return arr;
}

int[] ChangSgnArr(int[] arr)
{
    for (int i = 0; i < arr.Length; i++)
    {
       arr [i] = arr [i] * -1;
    }
    return arr;
}

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}

int[] newarr = GenArray();
PrintArray(newarr);
int[] charr = ChangSgnArr(newarr);
PrintArray(charr);