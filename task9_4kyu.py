# Write a function that takes a positive integer and
# returns the next smaller positive integer containing the same digits.
# For example:
# next_smaller(21) == 12
# next_smaller(531) == 513
# next_smaller(2071) == 2017
# Return -1 (for Haskell: return Nothing, for Rust: return None),
# when there is no smaller number that contains the same digits.
# Also return -1 when the next smaller number
# with the same digits would require the leading digit to be zero.
# next_smaller(9) == -1
# next_smaller(135) == -1
# next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros
# some tests will include very large numbers.
# test data only employs positive integers.


def func(first_n, i):
    first_n = list(str(first_n))
    for j in str(i):
        if j in first_n:
            first_n.remove(j)
        if not first_n:
            return True
    else:
        return False


def next_smaller(n):
    if len(str(n)) > 5:
        n = int(str(n)[-6:])
    result = [i for i in range(n - 1, 0, -1) if func(i, n)]
    if not result:
        return -1
    return result[0]


print(next_smaller(123456789))

