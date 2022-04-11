# Story
# Your online store likes to give out coupons for
# special occasions. Some customers try to cheat
# the system by entering invalid codes or using
# expired coupons.
# Task
# Your mission:
# Write a function called checkCoupon which verifies that a
# coupon code is valid and not expired.
# A coupon is no more valid on the day AFTER the expiration
# date. All dates will be passed as strings in this format:
# "MONTH DATE, YEAR".


def fanc_date(date: str):
    dat = {
        "January": "0",
        "February": "1",
        "March": "2",
        "April": "3",
        "May": "4",
        "June": "5",
        "July": "6",
        "August": "7",
        "September": "8",
        "October": "9",
        "November": "10",
        "December": "11"
    }
    date = date.split(' ')
    return (int(dat[date[0]]), int(date[1][:-1]), int(date[2]))

print(fanc_date('March 5, 1998'))
print(fanc_date('March 25, 1998'))


def check_coupon(entered_code, correct_code, current_date: str, expiration_date):
    first = entered_code == correct_code
    date_1 = fanc_date(current_date)
    date_2 = fanc_date(expiration_date)
    if first == False:
        return False
    if date_1[2] < date_2[2]:
        return True
    if date_1[2] == date_2[2]:
        if date_1[0] < date_2[0]:
            return True
        if date_1[0] == date_2[0]:
            if date_1[1] > date_2[1]:
                return False
            if date_1[1] == date_2[1]:
                return True
            else:
                return True
        else:
            return False
    else:
        return False


print(check_coupon('a12v564', 'a12v564', 'March 5, 1998', 'March 25, 1998'))

