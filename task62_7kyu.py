# This is related to my other Kata about cats and dogs.
# Kata Task
# I have a cat and a dog which I got as kitten / puppy.
# I forget when that was, but I do know their current ages as catYears and dogYears.
# Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]
# NOTES:
# Results are truncated whole numbers of "human" years
# Cat Years
# 15 cat years for first year
# +9 cat years for second year
# +4 cat years for each year after that
# Dog Years
# 15 dog years for first year
# +9 dog years for second year
# +5 dog years for each year after that


def owned_cat_and_dog(cat_years, dog_years):
    get_cat = 0 if cat_years <= 15 else \
        1 if cat_years <= 23 else \
        2 if cat_years == 24 else ((cat_years - 24) // 4) + 2
    get_dog = 0 if dog_years <= 15 else \
        1 if dog_years <= 23 else \
        2 if dog_years == 24 else ((dog_years - 24) // 5) + 2
    return [get_cat, get_dog]
