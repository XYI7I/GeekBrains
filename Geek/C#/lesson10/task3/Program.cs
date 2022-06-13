// 72. Заданы 2 массива: info и data. В массиве info хранятся двоичные представления нескольких чисел (без разделителя). В массиве data хранится информация о количестве бит, которые занимают числа из массива info. Напишите программу, которая составит массив десятичных представлений чисел массива data с учётом информации из массива info. 
Console.WriteLine("Программа составит массив десятичных представлений чисел массива data с учётом информации из массива info.");

int[] data = {0, 1, 1, 1, 1, 0, 0, 0, 1};
int[] info = {5, 3, 1};

void PrintArray(int[] prarr)
{
    var str = string.Join(" ", prarr);
    Console.WriteLine(str);
}


int[] BinArrToDecArr(int[] binarr, int[] info)
{
    int[] resultArr = new int[info.Length];
    int n = 0;
    for (int i = 0; i < info.Length; i++)
    {
        for (int j = 0; j < info[i]; j++)
        {   
            resultArr[i] += Convert.ToInt32(Math.Pow(2,info[i] - j - 1)) * binarr[n++];        
        } 
    }
    return resultArr;
}

int[] resultArr = BinArrToDecArr(data, info);
PrintArray(resultArr);