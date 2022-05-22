// 33. Задайте массив. Напишите программу, которая определяет, присутствует ли заданное число в массиве.
Console.WriteLine("Программа определяет, присутствует ли заданное число в массиве.");

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

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}

bool FindDigArrB(int[] arr, int num)
{
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] == num)
        {
            return true;
            break;
            //i = word.Length;
        }
    }
    return false;
}



int[] newarr = GenArray();
PrintArray(newarr);

Console.Write("Введите число для поиска в массивe: ");
int fnum = int.Parse(Console.ReadLine ());

bool barray = FindDigArrB(newarr, fnum);
string res =  barray ? $"Число {fnum} присутсвтует в массиве -> да" : $"Числа {fnum} нет в массиве -> нет";
Console.WriteLine(res);