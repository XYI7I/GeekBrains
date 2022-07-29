"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

"""


def encode_rle(s):
    """
    Функция RLE алгоритма сжатия данных.
    """
    encoding = ""

    i = 0
    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1

    return encoding

def decode_rle(rle_data):
    """
    Функция RLE алгоритма восстановления данных.
    """
    data = ""

    for i in range(0, len(rle_data), 2):
        data += rle_data[i + 1]*int(rle_data[i])
    return data


text_data = 'Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных'
print(encode_rle(text_data))
rle_data = encode_rle(text_data)

print(decode_rle(rle_data))
