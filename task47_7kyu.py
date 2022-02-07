# The function takes cents value (int) and needs to return
# the minimum number of coins combination of the same value.
# The function should return an array where
# coins[0] = pennies ==> $00.01
# coins[1] = nickels ==> $00.05
# coins[2] = dimes ==> $00.10
# coins[3] = quarters ==> $00.25


def coin_combo(cents):
    coins = [25, 10, 5, 1]
    result = []
    for i in coins:
        x = cents // i
        result.append(x)
        cents = cents % i
    result.reverse()
    return result


coin_combo(60)


