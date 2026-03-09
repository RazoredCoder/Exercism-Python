'''Given a target word and one or more candidate words, find the candidates that are anagrams of the target.'''
def find_anagrams(word:str, candidates:list):
    '''Given a target word and one or more candidate words, find the candidates that are anagrams of the target.
    :param word: str - a word to find anagrams of
    :param candidates: list - a list of possible anagrams
    :return: list - a list of correct anagrams
    '''
    anagrams = []
    letters_word = {}
    for letter in word.lower():
        if letter in letters_word:
            letters_word[letter] += 1
        else:
            letters_word[letter] = 0
    
    for candidate in candidates:
        if word.lower() == candidate.lower():
            continue
        letters_candidate = {}
        for letter in candidate.lower():
            if letter in letters_candidate:
                letters_candidate[letter] += 1
            else:
                letters_candidate[letter] = 0
        if letters_candidate.items() == letters_word.items():
            anagrams.append(candidate)
    return anagrams