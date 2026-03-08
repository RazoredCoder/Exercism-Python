'''The program takes color names as input and outputs a two digit number'''
def value(colors:list):
    '''The program takes color names as input and outputs a two digit number
    :param colors: list - list of color bands
    :return: int - the value of resistor
    '''
    color_values = {
            "black": 0,
            "brown": 1,
            "red": 2,
            "orange": 3,
            "yellow": 4,
            "green": 5,
            "blue": 6,
            "violet": 7,
            "grey": 8,
            "white": 9,
            }
    return int("".join(str(color_values[color]) for color in colors[:2]))