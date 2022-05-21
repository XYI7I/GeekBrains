// Программа по генерации одномерного массива:
Console.WriteLine("Программа по генерации одномерного одномерного массива");

int[] arr = new int[8];
Random rand = new Random();

for (int i = 0; i < arr.Length; i++)
{
    arr[i] = rand.Next(2);
    //Console.WriteLine(arr[i]);
}

var str = string.Join(" ", arr);
Console.WriteLine(str); 



