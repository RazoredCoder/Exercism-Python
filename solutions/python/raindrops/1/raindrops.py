'''Convert a number into its corresponding raindrop sounds.'''
def convert(number:int):
    '''Convert a number into its corresponding raindrop sounds.
    :param number: int - a number to be converter.
    :return: str - a converte message'''
    response = ''
    if number % 3 == 0:
        response += 'Pling'
    if number % 5 == 0:
        response += 'Plang'
    if number % 7 == 0:
        response += 'Plong'
    if not response:
        return str(number)
    return response