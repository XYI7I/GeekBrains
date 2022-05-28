// 45. Напишите программу, которая будет создавать копию заданного массива с помощью поэлементного копирования.
Console.WriteLine("Программа создает копию заданного массива");

int[] GenArray()
{
    Console.Write("Введите число элементов массива: ");
    int n = int.Parse(Console.ReadLine ());
    int[] arr = new int[n];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(11);
    }
    return arr;
}

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}

int[] CoppyArr(int[] arr)
{
    int[] coparr = new int[arr.Length];

    for (int i = 0; i < arr.Length; i++)
    {
        coparr[i] = arr[i];
    }
    return coparr;
 }


int[] arr = GenArray();
PrintArray(arr);
int[] newarr = CoppyArr(arr);
PrintArray(newarr);
