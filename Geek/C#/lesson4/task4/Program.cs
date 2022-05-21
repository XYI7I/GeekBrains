// Программа по генерации одномерного массива:
Console.WriteLine("Программа по генерации одномерного одномерного массива");

void Gen_Array()
{
    Console.Write("Введите число элементов массива: ");
    int N = int.Parse(Console.ReadLine ());
    int[] arr = new int[N];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(2);
        //Console.WriteLine(arr[i]);
    }

    var str = string.Join(" ", arr);
    Console.WriteLine(str);
}

Gen_Array();