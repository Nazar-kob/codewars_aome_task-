# Count the number of Duplicates
# Write a function that will return the count of distinct
# case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string.
# The input string can be assumed to contain only
# alphabets (both uppercase and lowercase) and numeric digits.


def duplicate_count(text: str):
    return sum([1 for i in set(text.lower()) if text.lower().count(i) > 1])


