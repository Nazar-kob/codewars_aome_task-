# In this Kata, you will be given a string that may have mixed
# uppercase and lowercase letters and your task is to convert
# that string to either lowercase only or uppercase only based on:
#
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase
# letters, convert the string to lowercase.

def solve(string: str):
    count_low = 0
    count_apper = 0
    for i in string:
        if i == i.lower():
            count_low += 1
        else:
            count_apper += 1
    return string.lower() if count_low >= count_apper else string.upper()


def solve_2(string: str):
    return string.lower() if sum([
        1 for i in string if i == i.lower()
    ]) >= len(string) - sum([1 for i in string if i == i.lower()]) else string.upper()


print(solve_2("NNZarK"))