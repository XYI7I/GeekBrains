//Напишите программу, которая на вход принимает одно число (N), а на выходе показывает все целые числа в промежутке от -N  до N.
Console.WriteLine("Выводит все целые числа в промежутке от -N до N.");

Console.Write("Введите N: ");
int N = int.Parse(Console.ReadLine ());
int i = -1 * N;
Console.WriteLine(i);

 while (i <= N)
 {
     Console.Write(i + " ");
    //  Console.Write(" ");
     i++;
 }

 Console.WriteLine();