'''Calculates the energy points that get awarded to players when they complete a level.'''
def sum_of_multiples(limit:int, multiples:list):
    '''Calculates the energy points that get awarded to players when they complete a level.
    :param limit: int - level of the player
    :param multiples: list - a list of player's items
    :return: int - points awarded to the plyer
    '''
    values = set()
    for magic_item in multiples:
        values = values.union({magic_item * index for index in range(1, limit+1) if magic_item * index < limit})
    return sum(values)