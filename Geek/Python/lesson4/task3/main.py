"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
"""

import re
from collections import Counter


def count_most_frequent_words(text, n=10):
    # Приводим текст к нижнему регистру
    text = text.lower()

    # Извлекаем слова из текста, игнорируя знаки препинания
    words = re.findall(r'\w+', text)

    # Подсчитываем количество встречаемых слов
    word_counts = Counter(words)

    # Возвращаем список наиболее часто встречающихся слов
    most_common_words = word_counts.most_common(n)

    return most_common_words


# Пример использования
text = """
Yuri Alekseyevich Gagarin[a] (9 March 1934 – 27 March 1968) was a Soviet pilot and cosmonaut who, aboard the first successful crewed spaceflight, became the first human to journey into outer space. Travelling on Vostok 1, Gagarin completed one orbit of Earth on 12 April 1961. By achieving this major milestone for the Soviet Union amidst the Space Race, he became an international celebrity and was awarded many medals and titles, including the nation's highest distinction: Hero of the Soviet Union.

Hailing from the village of Klushino in the Russian SFSR, Gagarin was a foundryman at a steel plant in Lyubertsy in his youth. He later joined the Soviet Air Forces as a pilot and was stationed at the Luostari Air Base, near the Norway–Soviet Union border, before his selection for the Soviet space programme alongside five other cosmonauts. Following his spaceflight, Gagarin became the deputy training director of the Cosmonaut Training Centre, which was later named after him. He was also elected as a deputy of the Soviet of the Union in 1962 and then to the Soviet of Nationalities, respectively the lower and upper chambers of the Supreme Soviet.

Vostok 1 was Gagarin's only spaceflight, but he served as the backup crew to Soyuz 1, which ended in a fatal crash, killing his friend and fellow cosmonaut Vladimir Komarov. Fearful that a high-level national hero might be killed, Soviet officials banned Gagarin from participating in further spaceflights. After completing training at the Zhukovsky Air Force Engineering Academy in February 1968, he was again allowed to fly regular aircraft. However, Gagarin died five weeks later, when the MiG-15 that he was piloting with flight instructor Vladimir Seryogin crashed near the town of Kirzhach.
"""

most_frequent_words = count_most_frequent_words(text, n=10)

print("Самые часто встречающиеся слова:")
for word, count in most_frequent_words:
    print(f"{word}: {count}")