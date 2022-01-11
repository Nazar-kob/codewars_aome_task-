# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, u as vowels for this Kata (but not y).
#
# The input string will only consist of lower case letters and/or spaces.


def get_count(sentence):
    vowels = 'aeiou'
    count_vowels = 0
    sentence = sentence.lower()

    for i in vowels:
            count_vowels += sentence.count(i)

    return count_vowels