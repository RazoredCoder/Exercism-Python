"""The program takes 3 colors as input, and outputs the correct value, in ohms."""
def label(colors:list):
    """The program takes 3 colors as input, and outputs the correct value, in ohms.
    :param colors: list - 3 color bands on the resistor
    :return: str - the value of resistance with the correct kilo, mega or giga if necessery
    """
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
    notation = {
                "giga": 1000_000_000,
                "mega": 1000_000,
                "kilo": 1000
                }
    resistor_value = int("".join(str(color_values[color]) for color in colors[:2]) + "0" * color_values[colors[2]])

    value_ohms = str(resistor_value) + " "
    biggest_tens = 0
    for name, tens in notation.items():
        if biggest_tens > tens:
            continue
        if resistor_value > 0 and resistor_value % tens == 0:
            value_ohms = f"{int(resistor_value/tens)} {name}"
            biggest_tens = tens

    return value_ohms + "ohms"