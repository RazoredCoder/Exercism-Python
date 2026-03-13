'''Implementation of the Atbash cipher, an ancient encryption system created in the Middle East.'''
import string
def encode(plain_text):
    '''Encoding normal text using the Atbash cipher
    :param plain_text: str - normal text to encode
    :return: str - encoded text
    '''
    plain = string.ascii_lowercase
    cypher_dict = {plain[index]: cypher for index, cypher in enumerate(string.ascii_lowercase[-1::-1])}
    count = 0
    encoded = []
    current = ''
    for character in plain_text:
        if character.lower() in plain:
            current += cypher_dict[character.lower()]    
            count += 1     
        elif character not in (' ', ',', '.', '!', '?', ''):
            current += character
            count += 1
        
        if count == 5:
            encoded.append(current)
            current = ''
            count = 0
    if current:
        encoded.append(current)

    return ' '.join(encoded)


def decode(ciphered_text):
    '''Decoding Atbash ciphered text
    :param ciphered_text: str - ciphered text to decode
    :return: str - decoded text
    '''
    plain = string.ascii_lowercase
    uncypher_dict = {string.ascii_lowercase[-1::-1][index]: letter for index, letter in enumerate(plain)}
    decoded = ''
    for character in ciphered_text:
        if character in plain:
            decoded += uncypher_dict[character]
        elif character != ' ':
            decoded += character
    return decoded