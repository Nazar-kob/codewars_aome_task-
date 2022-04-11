# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items. We want to
# create the text that should be displayed next to such an item.
# Implement the function which takes an array containing the names
# of people that like an item. It must return the display text as
# shown in the examples:


def likes(names):
    result = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this",
    }

    count = len(names)

    return result[min(4, count)].format(*names[:3], others=count - 2)

