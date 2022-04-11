# Create a function that takes an input String and returns a String,
# where all the uppercase words of the input String are in front and
# all the lowercase words at the end. The order of the uppercase and
# lowercase words should be the order in which they occur.
# If a word starts with a number or special character, skip the word
# and leave it out of the result.
# Input String will not be empty.
# For an input String: "hey You, Sort me Already!"
# the function should return: "You, Sort Already! hey me"


def capitals_first(text):
    lower_list = [i for i in text.split(' ') if i[0] == i[0].lower() and i[0].isalpha()]
    upper_list = [j for j in text.split(' ') if j[0] == j[0].upper() and j[0].isalpha()]
    result = ' '.join(upper_list) + ' ' + ' '.join(lower_list)
    return result.strip()
