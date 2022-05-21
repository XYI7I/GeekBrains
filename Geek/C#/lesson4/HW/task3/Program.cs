// Задача 29: Напишите программу, которая задаёт массив из N элементов и выводит их на экран.

Console.WriteLine("Программа задаёт массив из N элементов и выводит их на экран.");

int[] GenArray()
{
    Console.Write("Введите число элементов массива: ");
    int n = int.Parse(Console.ReadLine ());
    Console.Write("Введите диапазон чисел от 0 до N: ");
    int rangarr = int.Parse(Console.ReadLine ());
    int[] arr = new int[n];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(rangarr + 1);
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
