# According to ISO 8601, the first calendar week (1)
# starts with the week containing the first thursday
# in january. Every year contains of 52 (53 for leap years) calendar weeks.
# Your task is to calculate the calendar week (1-53)
# from a given date. For example, the calendar week for
# the date 2019-01-01 (string) should be 1 (int).
# Good luck 👍
# See also ISO week date and Week Number on Wikipedia
# for further information about calendar weeks.
# On whatweekisit.org you may click through the
# calender and study calendar weeks in more depth.
# heads-up: require(xxx) has been disabled
# Thanks to @ZED.CWT, @Unnamed and @proxya for their feedback.

import datetime


def get_calendar_week(date_string):
    date_string = [int(i) for i in date_string.split('-')]
    return list(datetime.date(date_string[0], date_string[1], date_string[2]).isocalendar())[1]


print(get_calendar_week("2017-10-01"))
