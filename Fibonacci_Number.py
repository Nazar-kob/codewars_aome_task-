def fib(n):
    a = 0
    b = 1
    result = [0]
    for i in range(n):
        a, b = b, a + b
        result.append(a)
    return result[n]