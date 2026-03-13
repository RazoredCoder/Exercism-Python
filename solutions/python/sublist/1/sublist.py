"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    """Determine the relationship between two lists.
    :param list_one: list - The first list to compare.
    :param list_two: list - The second list to compare.
    :return: int - One of the enumerated constants (SUBLIST, SUPERLIST, EQUAL, UNEQUAL).
    """
    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL

def is_sublist(smaller, larger):
    """Checks if smaller is a sublist of larger.
    :param smaller: list - a smaller list
    :param larger: list - a larger list
    :return: bool - is smaller a sublist of larger.
    """
    if len(smaller) > len(larger):
        return False
    if not smaller:
        return True
    for index in range(len(larger) - len(smaller) + 1):
        if larger[index:index + len(smaller)] == smaller:
            return True
    return False