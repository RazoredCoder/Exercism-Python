'''Implementation of the rotational cipher, also sometimes called the Caesar cipher.'''
def rotate(text:str, key:int):
    '''Implementation of the rotational cipher, also sometimes called the Caesar cipher.
    :param text: str - text to cypher
    :param key: int - Cypher Rotationa key
    :return: str - cyphered text
    '''
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cyphered_text = list(text)
    for position, char in enumerate(text):
        if char in alphabet_lower:
            index = ['lower', alphabet_lower.index(char)]
        elif char in alphabet_upper:
            index = ['upper', alphabet_upper.index(char)]
        else: continue
        
        if index[1] + key >= 26:
            index[1] -= 26
        if index[0] == 'lower':
            cyphered_text[position] = alphabet_lower[index[1] + key]
            continue
        cyphered_text[position] = alphabet_upper[index[1] + key]
    return ''.join(cyphered_text)