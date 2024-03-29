﻿// 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве, и возвращает значение этого элемента или же указание, что такого элемента нет.
Console.WriteLine("Программа создает двумерный массив размером m×n, заполненный случайными вещественными числами.");

int[,] GenArray()
{
    Console.Write("Введите число строк массива m: ");
    int m = int.Parse(Console.ReadLine ());
    Console.Write("Введите число строк массива n: ");
    int n = int.Parse(Console.ReadLine ());
    int[,] arr = new int[m, n];
    Random rand = new Random();

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            arr[i, j] = rand.Next(-10, 11);
        }

    }
    return arr;
}

void PrintArray(int[,] prarr)
{
    for (int i = 0; i < prarr.GetLength(0); i++)
    {
        for (int j = 0; j < prarr.GetLength(1); j++)
        {
            Console.Write(prarr[i,j] + " ");
        }
        Console.WriteLine();
    }
}

void GetElemArray(int[,] arr)
{
    Console.Write("Из какой строки m вывести элемент? m: ");
    int m = int.Parse(Console.ReadLine ());
    Console.Write("Из какого столбца n вывести элемент? n: ");
    int n = int.Parse(Console.ReadLine ());
    string res =  m < arr.GetLength(0) && n < arr.GetLength(1)? $"{arr[m, n]}" : $"array[{m}, {n}] -->  такого элемента в массиве нет";
    Console.WriteLine(res);
}

void FindNumArray(int[,] arr)
{
    Console.Write("Введите число, для поиска его в заданном массиве: ");
    int num = int.Parse(Console.ReadLine ());
    for (int i = 0; i < arr.GetLength(0); i++)
    {
        for (int j = 0; j < arr.GetLength(1); j++)
        {
            if (arr[i,j] == num)
            {
                Console.WriteLine($"{num} -> число есть в массиве");
                return;
            }
        }
    }
    Console.WriteLine($"{num} -> такого числа в массиве нет");
}

int[,] array = GenArray();
GetElemArray(array);
PrintArray(array);
FindNumArray(array);