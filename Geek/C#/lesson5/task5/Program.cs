// 37. Найдите произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Результат запишите в новом массиве.
Console.WriteLine("Программа находит произведение пар чисел в одномерном массиве. Парой считаем первый и последний элемент, второй и предпоследний и т.д. Результат выводит в новом массиве.");

int[] GenArray()
{
    Console.Write("Введите число элементов массива: ");
    int n = int.Parse(Console.ReadLine ());
    int[] arr = new int[n];
    Random rand = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rand.Next(100);
    }
    return arr;
}

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}

int[] MultPairArr(int[] arr)
{
    int[] multarr = new int[arr.Length / 2 + arr.Length % 2];
    int j = arr.Length - 1;
    for (int i = 0; i < multarr.Length; i++)
    {
        if (i == j)
        {
            multarr[i] = arr[i];
            break;
        }
        multarr[i] = arr[i] * arr[j];
        j--;
    }
    return multarr;
}


int[] genarr = GenArray();
PrintArray(genarr);
int[] multgenarr = MultPairArr(genarr);
PrintArray(multgenarr);