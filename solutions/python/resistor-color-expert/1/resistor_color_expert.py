'''Translating resistor color bands to human-readable labels.'''
def resistor_label(colors:list):
    '''translating resistor color bands to human-readable labels.
    :param colors: list - a list of color bands on the resistor
    :return: str - resistor's value in ohms as well as its tolerance.
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
    notation = {
            "giga": 1000_000_000,
            "mega": 1000_000,
            "kilo": 1000
            }
    tolerance = {        
            "grey": "0.05%",
            "violet": "0.1%",
            "blue": "0.25%",
            "green": "0.5%",
            "brown": "1%",
            "red": "2%",
            "gold": "5%",
            "silver": "10%"
            }
    
    if len(colors) < 1:
        return None
    if len(colors) == 1:
        return f"{color_values[colors[0]]} ohms"
    if len(colors) == 4:
        resistor_value = int("".join(str(color_values[color]) for color in colors[:2]) + "0" * color_values[colors[2]])

        value_ohms = str(resistor_value) + " "
        biggest_tens = 0
        for name, tens in notation.items():
            if biggest_tens > tens:
                continue
            if resistor_value > 0 and resistor_value >= tens:
                if int(resistor_value/tens) == resistor_value/tens:
                    value_ohms = f"{int(resistor_value/tens)} {name}"
                    continue
                value_ohms = f"{resistor_value/tens} {name}"
                biggest_tens = tens
        value_ohms += "ohms"
        value_ohms = f"{value_ohms} ±{tolerance[colors[3]]}"        
    if len(colors) == 5:
        resistor_value = int("".join(str(color_values[color]) for color in colors[:3]) + "0" * color_values[colors[3]])

        value_ohms = str(resistor_value) + " "
        biggest_tens = 0
        for name, tens in notation.items():
            if biggest_tens > tens:
                continue
            if resistor_value > 0 and resistor_value >= tens:
                if int(resistor_value/tens) == resistor_value/tens:
                    value_ohms = f"{int(resistor_value/tens)} {name}"
                    continue
                value_ohms = f"{resistor_value/tens} {name}"
                biggest_tens = tens
        value_ohms += "ohms"
        value_ohms = f"{value_ohms} ±{tolerance[colors[4]]}"        

    return value_ohms