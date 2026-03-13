'''The diamond kata takes as its input a letter, and outputs it in a diamond shape.
Given a letter, it prints a diamond starting with ‘A’, with the supplied letter at the widest point.'''
import string
def rows(letter):
    '''The diamond kata takes as its input a letter, and outputs it in a diamond shape.
    Given a letter, it prints a diamond starting with ‘A’, with the supplied letter at the widest point.
    :param letter: str - a single capital letter
    :return: list - a list of strings in the shape of a diamond
    '''
    all_letters = string.ascii_uppercase
    index = all_letters.index(letter)
    width = index*2 + 1
    spaces = [0] + [number for number in range(width) if number%2 != 0]
    diamond = []
    for row in range(index + 1):
        if row not in (0, index):
            leading =  int((width - spaces[row] - 2)/2)
            sequence = leading * ' ' + all_letters[row] + spaces[row] * ' ' + all_letters[row] + leading * ' '
        elif row == index and row > 0:
            sequence = all_letters[row] + spaces[row] * ' ' + all_letters[row]
        else:
            leading =  int((width - spaces[row] - 1)/2)
            sequence = leading * ' ' + all_letters[row] + leading * ' '
        diamond.append(sequence)
    if len(diamond) == 1: return diamond

    return diamond + diamond[-2::-1]