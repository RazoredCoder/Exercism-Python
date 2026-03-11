'''Change the data format of letters and their point values in the game.'''
def transform(legacy_data:dict):
    '''Change the data format of letters and their point values in the game.
    :param legacy_data: dict - a current one-to-many mapping
    :return: dict - new one-to-one mapping
    '''
    return {letter.lower(): value for value, letters in legacy_data.items() for letter in letters}