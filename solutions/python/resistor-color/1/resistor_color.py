'''Determine the values of resistors.'''

def color_code(color):
    '''Look up the numerical value associated with a particular color band'''
    
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
    return color_values[color]

def colors():
    '''List the different band colors'''
    return [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]