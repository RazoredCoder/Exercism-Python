'''Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verifies that any and all pairs are matched and nested correctly.'''
def is_paired(input_string):
    '''Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verifies that any and all pairs are matched and nested correctly.
    :param input_string: str - text to test
    :return: bool - verificatiob if any and all pairs are matched and nested correctly
    '''
    parentheses_open = {'{': 'curly', '[': 'square', '(': 'round'}
    parentheses_close = {'}': 'curly', ']': 'square', ')': 'round'}
    opened = []

    for character in input_string:
        if character in parentheses_open:
            opened.append(parentheses_open[character])
        elif character in parentheses_close and opened:
            if parentheses_close[character] == opened[-1]:
                opened.pop()
            else: return False
        elif character in parentheses_close and not opened:
            return False
    if not opened: return True
    return False