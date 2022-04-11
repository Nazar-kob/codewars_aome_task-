def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    result = [i for i in range(1, num) if num % i == 0]
    return len(result) > 1









