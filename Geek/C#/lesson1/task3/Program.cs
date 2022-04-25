// See https://aka.ms/new-console-template for more information
//Напишите программу, которая будет выдавать
//название дня недели по заданному номеру.

Console.WriteLine("дня недели по заданному номеру");

Console.Write("день число: ");
int numa = int.Parse(Console.ReadLine ());

if (numa == 1)
{
    Console.WriteLine("понедельник");
}

if (numa == 2)
{
    Console.WriteLine("вторник");
}

if (numa == 3)
{
    Console.WriteLine("среда");
}

if (numa == 4)
{
    Console.WriteLine("четверг");
}

if (numa == 5)
{
    Console.WriteLine("пятница");
}

if (numa == 6)
{
    Console.WriteLine("суббота");
}

if (numa == 7)
{
    Console.WriteLine("вск");
}
