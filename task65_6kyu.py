# Write an algorithm that will identify valid IPv4
# addresses in dot-decimal format. IPs should be considered
# valid if they consist of four octets,
# with values between 0 and 255, inclusive.



def is_valid_IP(strng: str):
    result = strng.split('.')
    if len(result) != 4:
        return False
    for num in result:
        if num.isdigit() and len(num) > 1 and num[0] == '0':
            return False
        else:
            if num.isdigit() and 0 <= int(num) <= 255:
                pass
            else:
                return False
    return True
