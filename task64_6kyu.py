# It's 9 time!
#
# I want to count from 1 to n. How many times will I use a '9'?
#
# 9, 19, 91.. will contribute one '9' each, 99, 199, 919.. wil contribute two '9's each...etc
#
# Note: n will always be a positive integer.
#
# count_nines(8) == 0
# count_nines(9) == 1
# count_nines(10) == 1
# count_nines(98) == 18
# count_nines(100) == 20



def count_nines(n):
    return sum([str(i).count('9') for i in range(1, n + 1) if i % 9 != 0])

print(count_nines(100))