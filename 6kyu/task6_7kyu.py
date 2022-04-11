# Run-length encoding (RLE) is a very simple form of lossless
# data compression in which runs of data are stored as a single data value and count.
# A simple form of RLE would encode the string "AAABBBCCCD" as "3A3B3C1D" meaning,
# first there are 3 A, then 3 B, then 3 C and last there is 1 D.
# Your task is to write a RLE encoder and decoder using this technique.
# The texts to encode will always consist of only uppercase characters, no numbers.


def encode(string):
    count = 1
    result = ''
    string += '_'
    for i in range(len(string) - 1):

        if string[i] != string[i + 1]:
            result += str(count) + string[i]
            count = 1
        else:
            count += 1

    return result



def decode(string):
    mini_string = ''
    result = ''

    for i in range(len(string)):

        value = string[i]
        mini_string += value

        if value.isalpha():
            result += int(mini_string[:-1]) * mini_string[-1]
            mini_string = ''

    return result


