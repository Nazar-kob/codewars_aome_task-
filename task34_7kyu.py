# Friday 13th or Black Friday is considered as unlucky day.
# Calculate how many unlucky days are in the given year
# Find the number of Friday 13th in the given year.
# Input: Year in Gregorian calendar as integer.
# Output: Number of Black Fridays in the year as an integer.

import datetime
def unlucky_days(year):
    return sum([1 for i in range(1, 12+1) if datetime.date(year, i, 13).weekday() == 4])