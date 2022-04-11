# Given a lowercase string that has alphabetic characters only and no spaces, return the highest
# value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".
# We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
# For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

x = "zodiacs"

def solve(s: str):
    alch = "_abcdefghijklmnopqrstuvwxyz"
    ind_alch = {alch[item]: item for item in range(1, 27)}

    for item in "aeiou":
        s = s.replace(item, ' ')

    result = []

    for i in s.split(' '):
        count = 0
        if len(i) > 0:
            for j in i:
                count += ind_alch[j]
            result.append(count)

    return max(result)

