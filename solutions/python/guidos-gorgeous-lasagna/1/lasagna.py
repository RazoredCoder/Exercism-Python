"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    if elapsed_bake_time < EXPECTED_BAKE_TIME:
        return EXPECTED_BAKE_TIME - elapsed_bake_time
    else:
        return 0

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    :param number_of_layers: int - number of lasagna layers.
    :return: int - preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the number of layers of the lasagna and returns how much time it takes to prapare
    based on the `PREPARATION_TIME`.
    """
    if number_of_layers > 0:
        return number_of_layers*PREPARATION_TIME
    else:
        return 0


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total minutes spent in the kitchen.

    :param number_of_layers: int - number of lasagna layers.
    :param elapsed_bake_time: int - time that lasagna already spent in the oven
    :return: int - total time spent in the kitchen (in minutes) derived from 'preparation_time_in_minutes()' and 'elapsed_bake_time'.

    Function that takes the number of layers of the lasagna and returns how much time it takes to prapare
    based on the `PREPARATION_TIME`.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)


