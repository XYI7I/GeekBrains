// Программа по генерации одномерного массива:
Console.WriteLine("Программа по генерации одномерного одномерного массива");

int[] GenArray()
{
    Console.Write("Введите число элементов массива: ");
    int N = int.Parse(Console.ReadLine ());
    int[] arr = new int[N];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(2);
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

