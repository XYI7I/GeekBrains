// 22. Напишите программу, которая принимает на вход число (N) и выдаёт таблицу квадратов чисел от 1 до N.
Console.WriteLine("Программа, принимает на вход число N и выдаёт таблицу квадратов чисел от 1 до N.");

Console.Write("Ведите число N: ");
int N = int.Parse(Console.ReadLine ());

void SquareArray(int Num)
{
    int[] array = new int[Num];
    int[] array2 = new int[Num];

    for (int i = 0; i < Num; i++)
    {
        array [i] = i + 1;
        array2 [i] = (i + 1) * (i + 1);
    }
    var str1 = string.Join(" ", array);
    var str2 = string.Join(" ", array2);
    Console.WriteLine($"Числа   -> {str1}");
    Console.WriteLine($"Квадрат -> {str2}");   
}

void SquareArray_new(int Num)
{
    int[,] mas = new int[Num, 2];

    for (int i = 0; i < Num; i++)
    {
        mas[i, 0] = i + 1;
        mas[i, 1] = (i + 1) * (i + 1);
    }

    Console.WriteLine($"   Число  -> Квадрат");
    for (int i = 0; i < Num; i++)
    {
	    
        for (int j = 0; j < 2; j++)
        {
            Console.Write(String.Format("{0,11}", "  " + mas[i, j] + "    |"));
        }
		    
	    Console.WriteLine();
    } 
}

// SquareArray(N);

SquareArray_new(N);