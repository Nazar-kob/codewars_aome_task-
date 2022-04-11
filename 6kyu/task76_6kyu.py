def one_down(txt):
    if not isinstance(txt, str):
        return "Input is not a string"

    s_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s_lower = "abcdefghijklmnopqrstuvwxyz"

    result = ''

    for char in txt:

        if char.isalpha():
            if char == char.upper():
                ind_txt = s_upper.index(char)
                result += s_upper[ind_txt - 1]
            else:
                ind_txt = s_lower.index(char)
                result += s_lower[ind_txt - 1]

        else:
            result += char

    return result


print(one_down("XiBu BcPvU dSbAz UfYu"))