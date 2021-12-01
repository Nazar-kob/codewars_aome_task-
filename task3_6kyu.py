# task3, 6kyu

# Given an integer n return "odd" if the number of its divisors is odd.
# Otherwise return "even".
# Note: big inputs will be tested.
# Examples:
# All prime numbers have exactly two divisors (hence "even").
# For n = 12 the divisors are [1, 2, 3, 4, 6, 12] – "even".
# For n = 4 the divisors are [1, 2, 4] – "odd".


def oddity(n):
    div_amount = []
    for item in range(1, n + 1):
        if n % item == 0:
            div_amount.append(item)
    if len(div_amount) % 2 == 0:
        return 'even'
    else:
        return 'odd'


print(oddity(1))
print(oddity(5))
print(oddity(16))


