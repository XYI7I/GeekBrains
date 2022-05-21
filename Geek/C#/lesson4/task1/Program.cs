// 22. Напишите программу, которая принимает на вход число (A)и выдает сумму всех чисел от 1 до A.
Console.WriteLine("Программу, которая принимает на вход число (A)и выдает сумму всех чисел от 1 до A.");

Console.Write("Введите A: ");
int a = int.Parse(Console.ReadLine ());

int sum = 0;

int i = 1;

 while (i <= a)
 {
     sum = sum + i;
     i++; 
 }

 Console.WriteLine(a + " -> " + sum);

int sum1 = 0;
for (int j = 1; j <= a; j++)
{
    sum1 = sum1 + j;
}

Console.WriteLine(a + " -> " + sum1);  