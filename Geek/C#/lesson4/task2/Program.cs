// 26. Напишите программу, которая принимает на вход число и выдает количество цифр в числе.
Console.WriteLine("Программу, которая принимает на вход число и выдает количество цифр в числе.");

Console.Write("Введите число: ");
int num = int.Parse(Console.ReadLine ());

int dev = 10;
int dig_w = 1;

while (num / dev != 0)
{
    dev = dev * 10;
    dig_w = dig_w + 1;
}
Console.WriteLine($"Количество цифр в числе {num} -> {dig_w}");

int dig = 0;
for (int i = 1; i < num; i = i * 10)
{
    dig++;
}

Console.WriteLine($"Количество цифр в числе {num} -> {dig}");