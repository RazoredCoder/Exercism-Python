'''Translate text from English to Pig Latin'''
import string
def translate(text):
    '''Translate text from English to Pig Latin
    :param text: str - a string of text
    :return: str - text translated to Pig Latin
    '''
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    consonants = set(string.ascii_lowercase) - vowels
    text_list = text.split(' ')
    result = []
    for word in text_list:
        if (word[0] in vowels and word[0] != 'y') or word.startswith('xr') or word.startswith('yt'):
            result.append(f'{word}ay')
            continue
        elif word[0] in consonants or word[0] == 'y':
            i = 1
            cons_end = 0
            is_qu = False
            while i < len(word) and word[i] in consonants:
                try:
                    if word[i] == 'q' and word[i+1] == 'u':
                        cons_end = i - 1
                        break
                except IndexError:
                    pass
                cons_end = i
                i += 1
            if word[cons_end+1:cons_end+3] == 'qu': is_qu = True
            if cons_end and (not is_qu or word[cons_end+1] == 'y'):
                result.append(f'{word[cons_end+1::]}{word[:cons_end+1]}ay')
                continue
            elif is_qu:
                result.append(f'{word[cons_end+3::]}{word[:cons_end+3]}ay')
                continue
            elif word[0:2] == 'qu':
                result.append(f'{word[2:]}{word[:2]}ay')
                continue
            result.append(f'{word[cons_end+1::]}{word[:cons_end+1]}ay')
    return ' '.join(result)