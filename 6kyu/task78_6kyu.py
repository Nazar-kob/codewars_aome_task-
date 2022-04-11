# Generate a valid randomly generated hexadecimal
# color string. Assume all of them always have 6 digits.

import random


def generate_color_rgb():
    color = []
    while len(color) != 3:
        col = hex(random.randint(0, 255))[2:].upper()

        if len(col) == 2:
            color.append(col)

    return "#{}{}{}".format(*color)
