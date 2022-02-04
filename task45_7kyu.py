# Take 2 strings s1 and s2 including only letters from ato z.
# Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2.


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"

def longest(a1, a2):
    return ''.join(sorted(list(set(a1 + a2))))

longest(a, b)