# task2, 5kyu
# This time we want to write calculations using
# functions and get the results. Let's have a look at some examples:
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical
# operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand,
# the most inner function represents the right operand
# Division should be integer division. For example,
# this should return 2, not 2.666666...:
# eight(divided_by(three()))


from math import floor


def zero(f=''): return floor(eval('0' + f))


def one(func=''): return floor(eval('1' + func))


def two(func=''): return floor(eval('2' + func))


def three(func=''): return floor(eval('3' + func))


def four(f=''): return floor(eval('4' + f))


def five(f=''): return floor(eval('5' + f))


def six(f=''): return floor(eval('6' + f))


def seven(f=''): return floor(eval('7' + f))


def eight(f=''): return floor(eval('8' + f))


def nine(f=''): return floor(eval('9' + f))


def plus(func): return '+' + str(func)


def minus(f): return '-' + str(f)


def times(f): return '*' + str(f)


def divided_by(f): return '/' + str(f)


print(seven(times(five())))  # must return 35
print(four(plus(nine())))  # must return 13
print(eight(minus(three())))  # must return 5
print(six(divided_by(two())))  # must return 3


