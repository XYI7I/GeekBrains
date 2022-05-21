// Программа по генерации одномерного массива:
Console.WriteLine("Программа по генерации одномерного одномерного массива");

int[] Gen_Array()
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
    return arr;
}

int[] newarr = Gen_Array();

var str = string.Join(" ", newarr);
Console.WriteLine(str);