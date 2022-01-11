# Snail Sort
# Given an n x n array, return the array elements arranged
# from outermost elements to the middle element, traveling clockwise.
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:
# NOTE: The idea is not sort the elements from the
# lowest value to the highest; the idea is to traverse the 2-d
# array in a clockwise snailshell pattern.
# NOTE 2: The 0x0 (empty matrix) is represented as en empty
# array inside an array [[]].


def snail(snail_map):
    result = []

    while len(snail_map) >= 2:
        values = step_snail(snail_map)
        print(values)
        result.extend(values[0])
        snail_map = values[1]
    else:
        if len(snail_map) == 1:
            result.extend(*snail_map)

    return result


def step_snail(ls: list):
    result = []

    for i in range(4):
        if i == 0:
            for items_0 in ls[0]:
                result.append(items_0)
            ls = ls[1:]
        elif i == 1:
            for items_1 in range(len(ls)):
                result.append(ls[items_1][-1])
                ls[items_1] = ls[items_1][:-1]
        elif i == 2:
            for items_2 in ls[-1][::-1]:
                result.append(items_2)
            ls = ls[:-1]
        elif i == 3:
            for items_3 in range(-1, -abs(len(ls)) - 1, -1):
                result.append(ls[items_3][0])
                ls[items_3] = ls[items_3][1:]

    return result, ls
