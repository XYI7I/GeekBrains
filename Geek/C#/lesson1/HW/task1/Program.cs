// See https://aka.ms/new-console-template for more information
Console.WriteLine("Задание 1. Программа, которая принимает два числа и выдаёт какое большее, а какое меньшее.");

Console.Write("Первое число: ");
int numa = int.Parse(Console.ReadLine ());

Console.Write("Второе число: ");
int numb = int.Parse(Console.ReadLine ());

if (numa > numb)
{
    Console.WriteLine("Первое число: " + numa + " больше второгочисла: " + numb);
}

else if (numa == numb)
{
    Console.WriteLine("Числа равны!");
}

else
{
    Console.WriteLine("Первое число: " + numa + " меньше второго числа: " + numb);
}
