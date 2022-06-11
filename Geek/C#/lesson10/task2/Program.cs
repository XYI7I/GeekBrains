// 71. В некотором машинном алфавите имеются четыре буквы «а», «и», «с» и «в». Покажите все слова, состоящие из n букв, которые можно построить из букв этого алфавита.
Console.WriteLine("Программа покажет все слова, состоящие из n букв, которые можно построить из букв этого алфавита.");

string charArray = "012345789";

Console.Write("Введите N: ");
int n = int.Parse(Console.ReadLine ());

void PrintAllWord(string alphabet, char[] word, int length = 0)
{
    if (length == word.Length)
    {
        Console.WriteLine($"{new String(word)}"); return;
    }
    for (int i = 0; i < alphabet.Length; i++)
    {
        word[length] = alphabet[i];
        PrintAllWord(alphabet, word, length + 1);
    }
}

PrintAllWord(charArray, new char[n]);