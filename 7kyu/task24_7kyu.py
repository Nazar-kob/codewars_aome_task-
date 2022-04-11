# Given the triangle of consecutive odd numbers:
#
#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...



def row_sum_odd_numbers(n):
    list_odd = [i for i in range(1, 10000) if i % 2 != 0]
    result = []
    ls = []
    count = 1
    for j in list_odd:
        if len(ls) == count:
            result.append(ls)
            count += 1
            ls = []
        ls.append(j)
    return sum(result[n-1])
