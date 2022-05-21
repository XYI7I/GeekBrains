// **. Напишите функцию, которая принимает слово и возвращает true, если в этом слове есть две одинаковые, стоящие рядом буквы.
Console.WriteLine("Функция возвращает true, если в слове есть две одинаковые, стоящие рядом буквы.");

void CharDoubl(string word)
{
    bool check = false;
    for (int i = 0; i < word.Length - 1; i++)
    {
        if (word[i] == word[i + 1])
        {
            check = true;
            break;
            //i = word.Length;
        }
    }

    Console.WriteLine(check);
}

CharDoubl("12354");