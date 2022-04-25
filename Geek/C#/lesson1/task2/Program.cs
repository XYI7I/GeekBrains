//Напишите программу, которая на вход принимает два
//числа и проверяет, является ли первое число квадратом второго.


Console.WriteLine("Является ли первое число квадратом второго?");

Console.Write("первое число: ");
int numa = int.Parse(Console.ReadLine ());
Console.Write("второе число: ");
int numb = int.Parse(Console.ReadLine ());
bool square = numa * numa == numb;

Console.WriteLine(square ? "Yes", "No");

// if (numb == numa * numa)
// {
//     Console.WriteLine("первое число квадрат второго");
// }

// else
// {
//     Console.WriteLine("первое число не квадрат второго");
// }