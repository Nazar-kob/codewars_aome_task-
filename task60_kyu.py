# Task
# You will be passed the dice value frequencies,
# and your task is to write the code to return a
# string representing a histogram, so that when it
# is printed it has the same format as the example.
# Notes
# There are no trailing spaces on the lines
# All lines (including the last) end with a newline \n
# A count is displayed beside each bar except where the count is 0
# The number of rolls may vary but there are never more than 100


def histogram(results):
    result_str = "6|{}\n5|{}\n4|{}\n3|{}\n2|{}\n1|{}\n"
    data_str = ['#' * i + " " + str(i) if i else '' for i in results[::-1]]
    return result_str.format(*data_str)

