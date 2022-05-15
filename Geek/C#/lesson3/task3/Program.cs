// 18. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
Console.WriteLine("Программа, по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).");

int num_Q = 0;
string res = null;
// string inf = "∞";


Console.WriteLine(inf);

while (num_Q <= 0 || num_Q > 4)
{
    Console.Write("Ведите номер четверти, Q [1, 4]: ");
    num_Q = int.Parse(Console.ReadLine ());
}
if (num_Q == 1 || num_Q == 4)
{
    res = num_Q == 1? $"X [0, +inf] Y [0, +inf]" : $"X [0, +inf] Y [0, -inf]";
}

else
{
    res = num_Q == 2? $"X [0, -inf] Y [0, +inf]" : $"X [0, -inf] Y [0, -inf]";
}

Console.WriteLine(res);
