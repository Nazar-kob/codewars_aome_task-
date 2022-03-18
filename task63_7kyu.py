# Complete the function that returns the color of the given square on a normal, 8x8 chess board

# "a", 8  ==>  "white"
# "b", 2  ==>  "black"
# "f", 5  ==>  "white"

def square_color(file, rank):
    letters = 'abcdefgh'
    color_while, color_black = 'white', 'black'
    first = {}
    for char in letters:
        for num in range(1, 9):
            if num % 2 != 0:
                first.update({(char, num): color_black})
            else:
                first.update({(char, num): color_while})

        if char == 'a' or char == 'c' or char == 'e' or char == 'g':
            color_black, color_while = 'white', 'black'
        else:
            color_while, color_black = 'white', 'black'
    return first[(file, rank)]

