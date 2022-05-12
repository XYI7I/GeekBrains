// 9. Напишите программу, которая выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа.
Console.WriteLine("Программа, выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа.");
Random rnd = new Random();
int num = rnd.Next(10, 100);

Console.WriteLine("Число = " + num);
if (num / 10 > num % 10)
{
    Console.WriteLine(num + " -> " + (num / 10));
}
else
{
    Console.WriteLine(num + " -> " + (num % 10));
}