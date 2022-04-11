# Create a function that takes one positive three digit
# integer and rearranges its digits to get the maximum
# possible number. Assume that the argument is an integer.
# Return -1 if the argument is not valid
# Return null (nil for Ruby, nothing for Julia) if the argument is not valid.
# maxRedigit(123); // returns 321


def max_redigit(num):
    if num < 0 or len(str(num)) != 3:
        return None
    max_num = "".join(sorted(str(num))[::-1])

    return int(max_num)
