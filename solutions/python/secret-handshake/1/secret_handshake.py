'''Convert a number between 1 and 31 to a sequence of actions in the secret handshake.'''
def commands(binary_str:str):
    '''Convert a number between 1 and 31 to a sequence of actions in the secret handshake.
    :param binary_str: str - a binary form of a number
    :return: list - a secret handshake
    '''
    actions = ('wink', 'double blink', 'close your eyes', 'jump', 'reverse')
    handshake = []
    for index, number in enumerate(binary_str[-1::-1]):
        if index == 4 and number == '1':
            handshake.reverse()
            break
        if number == '1':
            handshake.append(actions[index])
    return handshake