# Task
# You will be given an array of integers in a [1; 50] range,
# and a number n. You have to extract n smallest elements
# out of the array preserving their original order.
# Notes
# There will be duplicates in the array, and they have
# to be returned in the order of their each separate appearence.
# This kata is an example of the "know your data" principle.
# Remember this while searching for the correct approach.

numbers = [1, 2, 4, 1, 2]

n = 3
result = [1, 2, 1]

def performant_smallest(arr: list, n):
    change_num = 100
    result_position = {}
    result_list = []
    for i in range(n):

        min_in_arr = min(arr)
        ind_min = arr.index(min_in_arr)
        arr[ind_min] = change_num
        ind_change_num = arr.index(change_num)
        result_position.update({ind_change_num: min_in_arr})
        change_num -= 1

    for j in sorted(list(result_position.keys())):
        result_list.append(result_position[j])

    return result_list







