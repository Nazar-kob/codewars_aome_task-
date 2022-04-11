# Complete the function scramble(str1, str2) that returns true if a
# portion of str1 characters can be rearranged to match str2, otherwise returns false.
# Notes:
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.

def scramble(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    for i in s2:
        if s2.count(i) <= s1.count(i):
            pass
        else:
            return False
    return True


    # return all([True if s2.count(i) == s1.count(i) else False for i in s2])

print(scramble('katas', 'steak'))