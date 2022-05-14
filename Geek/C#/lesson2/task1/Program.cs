// 9. Напишите программу, которая выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа.
Console.WriteLine("Программа, выводит случайное число из отрезка [10, 99] и показывает наибольшую цифру числа.");
Random rnd = new Random();
int num = rnd.Next(10, 100);

int GetMaxDigit (int number)
{
    int res =  number / 10 > number % 10 ? number / 10 : number % 10;
    return res;
}

Console.WriteLine("Число = " + num);
if (num / 10 > num % 10)
{
    Console.WriteLine(num + " -> " + (num / 10));
}
else
{
    Console.WriteLine(num + " -> " + (num % 10));
}

string res =  num / 10 > num % 10 ? $"{num} -> {num / 10}" : $"{num} -> {num % 10}";
Console.WriteLine(res);

int Max_Dig = GetMaxDigit(num);
Console.WriteLine(num + " -> " + Max_Dig);