// 42. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Console.WriteLine("Программа преобразовывать десятичное число в двоичное.");

// Длины сторон треугольника
Console.Write("Ведите число: ");
int decnum = int.Parse(Console.ReadLine ());


void BinNum(int num)
{
    string binnum = "";
    int decnum = num;
    while (num > 0)
    {
        string text = (num % 2).ToString();
        num = num / 2;

        binnum = text + binnum;
    }
    Console.WriteLine($"Число {decnum} в двоичном формате: {binnum}");
}

void BinNumRec(int num)
{
    string binnum = "";
    int decnum = num;
    if (num == 0)
    {
        return;
    }
    BinNumRec(num / 2);
    
    Console.Write(num % 2);
}


BinNum(decnum);
BinNumRec(decnum);
