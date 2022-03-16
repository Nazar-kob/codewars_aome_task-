# In this kata, you will do addition and subtraction on a given string.
# The return value must be also a string.
# Note: the input will not be empty.
# Examples
# "1plus2plus3plus4"  --> "10"
# "1plus2plus3minus4" -->  "2"

s = "1plus2plus3minus4"


def calculate(s):
    s = s.replace("plus", "+").replace("minus", "-")
    return str(eval(s))


print(calculate(s))
