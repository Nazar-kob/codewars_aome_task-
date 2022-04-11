# This time no story, no theory. The examples below show you how to write function accum:
#
# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.


def accum(string: str):
    result = ""
    for n, i in enumerate(string):
        str2 = i * n
        result += i.upper() + str2.lower() + "-"
    return result[:-1]


print(accum('abcd'))
