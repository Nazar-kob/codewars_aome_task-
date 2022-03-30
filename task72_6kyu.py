# Finish the solution so that it takes an input n (integer) and returns a string that is the decimal
# representation of the number grouped by commas after every 3 digits.
# Assume: 0 <= n < 2147483647

def group_by_commas(n):
    n = str(n)

    if len(n) <= 3:
        return n

    n = n[::-1]

    for i in range(3, len(n) + 2, 4):
        n = n[:i] + "," + n[i:]
        print(n)

    n = n[::-1]

    return n.strip(',')


def group_by_commas2(n):
    return f'{n:,}'
