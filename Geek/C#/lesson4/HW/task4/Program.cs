// **. Напишите функцию, которая принимает слово и возвращает true, если в этом слове есть две одинаковые, стоящие рядом буквы.
Console.WriteLine("Функция возвращает true, если в слове есть две одинаковые, стоящие рядом буквы.");

bool CharDoubl(string word)
{
    for (int i = 0; i < word.Length - 1; i++)
    {
        if (word[i] == word[i + 1])
        {
            return true;
            break;
            //i = word.Length;
        }
    }
    return false;
}

// Console.Write("Введите слово: ");
// string wordtest = Console.ReadLine ();
// bool che = CharDoubl(wordtest);
// Console.WriteLine(CharDoubl(wordtest));
// Console.WriteLine(CharDoubl("112348sfergg"));