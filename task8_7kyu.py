# Given a credit card number we can determine who the issuer/vendor
# is with a few basic knowns.
# Complete the function get_issuer() that will use the values shown
# below to determine the card issuer for a given card number.
# If the number cannot be matched then the function should return the string Unknown.
#
# | Card Type  | Begins With          | Number Length |
# |------------|----------------------|---------------|
# | AMEX       | 34 or 37             | 15            |
# | Discover   | 6011                 | 16            |
# | Mastercard | 51, 52, 53, 54 or 55 | 16            |
# | VISA       | 4                    | 13 or 16      |


def get_issuer(number):
    number = str(number)
    length_number = len(number)

    if (length_number == 13 or length_number == 16) and number[0] == "4":
        return "VISA"
    elif length_number == 16:
        if number[:4] == '6011':
            return "Discover"
        elif 51 <= int(number[:2]) <= 55:
            return "Mastercard"
    elif length_number == 15 and (number[:2] == "34" or number[:2] == "37"):
        return "AMEX"

    return 'Unknown'
