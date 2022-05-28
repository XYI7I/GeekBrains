// 43. Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
Console.WriteLine("Программа найдёт точку пересечения двух прямых, заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.");

// Коэффициенты второго уравнения
Console.Write("Введите коэффициент уравнениями y = k1 * x + b1; k1: ");
double cof_k1 = double.Parse(Console.ReadLine ());
Console.Write("Введите коэффициент уравнениями y = k1 * x + b1; b1: ");
double cof_b1 = double.Parse(Console.ReadLine ());

// Коэффициенты второго уравнения
Console.Write("Введите коэффициент уравнениями y = k2 * x + b2; k2: ");
double cof_k2 = double.Parse(Console.ReadLine ());
Console.Write("Введите коэффициент уравнениями y = k2 * x + b2; b2: ");
double cof_b2 = double.Parse(Console.ReadLine ());

void CrossPoint(double k1, double b1, double k2, double b2)
{
    double x = (b2 - b1) / (k1 - k2);
    double y = k1 * x + b1;
    double y1 = k2 * x + b2;
    Console.WriteLine($"Координаты точки пересечения: ({Math.Round(x, 2)}, {Math.Round(y, 2)}; {Math.Round(y1, 2)})");
}

CrossPoint(cof_k1, cof_b1, cof_k2, cof_b2);