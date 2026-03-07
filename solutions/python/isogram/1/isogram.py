'''Determine if a word or phrase is an isogram.'''
def is_isogram(string:str):
    '''Determine if a word or phrase is an isogram.
    :param string: str - a word or phrase
    :return: bool - is it an isogram
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = {char: 0 for char in alphabet}
    for char in string.lower():
        try:
            count[char] += 1
            if count[char] > 1:
                return False
        except KeyError:
            continue
    return True