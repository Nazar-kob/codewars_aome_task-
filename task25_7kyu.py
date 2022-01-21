# Input:
# a string strng
# an array of strings arr
# Output of function contain_all_rots(strng, arr) (or containAllRots or contain-all-rots):
# a boolean true if all rotations of strng are included in arr (C returns 1)
# false otherwise (C returns 0)
# Examples:
# contain_all_rots(
#   "bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true
# contain_all_rots(
#   "Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)
# Note:
# Though not correct in a mathematical sense
# we will consider that there are no rotations of strng == ""
# and for any array arr: contain_all_rots("", arr) --> true

def rots_str(string: str):
    result = []
    for i in string:
        string = string[1:]+string[0]
        result.append(string)
    return result


def contain_all_rots(string, arr):
    if not string:
        return True

    string = rots_str(string)

    for i in string:
        if i not in arr:
            return False
    return True









