# Your job is to fix the parentheses so that all opening
# and closing parentheses (brackets) have matching counterparts.
# You will do this by appending parenthesis to the beginning or
# end of the string. The result should be of minimum length.
# Don't add unnecessary parenthesis.
# The input will be a string of varying length, only containing '(' and/or ')'.
# For example:
# Input: ")("
# Output: "()()"
# Input: "))))(()("
# Output: "(((())))(()())"
# Enjoy!

def fix_parentheses(strng):
    pa_left = 0
    pa_right = 0
    for i in strng:
        if i == "(":
            pa_right += 1
        else:
            if pa_right == 0:
                pa_left += 1
            else:
                pa_right -= 1
    return pa_left * "(" + strng + pa_right * ")"
