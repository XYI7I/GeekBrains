// 39. Напишите программу, которая перевернёт одномерный массив (последний элемент будет на первом месте, а первый - на последнем и т.д.). 
Console.WriteLine("Программа, перевернёт одномерный массив (последний элемент будет на первом месте, а первый - на последнем и т.д.");

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

int[] ReverceArr(int[] arr)
{
    int[] revarr = new int[arr.Length];
    int j = arr.Length - 1;
    for (int i = 0; i <= j; i++)
    {
        revarr[i] = arr[j];
        revarr[j] = arr[i];
        j--;
    }
    return revarr;
}

int[] genarr = GenArray();
PrintArray(genarr);
int[] revarr = ReverceArr(genarr);
PrintArray(revarr);
Array.Reverse(revarr);
PrintArray(revarr);