'''Check if the sentence is a pangram.'''
def is_pangram(sentence:str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in sentence.lower():
            return False
        continue
    return True