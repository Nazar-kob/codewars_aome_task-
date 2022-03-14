# Find the last element of the given argument(s).
# Examples
# last([1, 2, 3, 4]) ==>  4
# last("xyz")        ==> "z"
# last(1, 2, 3, 4)   ==>  4

def last(*args):
    if isinstance(args[-1], (list, tuple, str)):
        return args[-1][-1]
    return args[-1]