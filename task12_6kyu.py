# Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value
# has more than one digit, continue reducing in this way
# until a single-digit number is produced. The input will be a non-negative integer.
# Examples


def digital_root(n):
    while len(str(n)) != 1:
        n = sum([int(i) for i in str(n)])
    return n


print(digital_root(493193))










