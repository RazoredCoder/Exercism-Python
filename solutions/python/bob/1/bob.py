'''Determine what Bob will reply to someone when they say something to him or ask him a question.
'''
def response(hey_bob:str):
    '''Determine what Bob will reply to someone when they say something to him or ask him a question.
    :param hey_bob: str - a text directed at Bob
    :return: str - predicted Bob's response
    '''

    if any(char.isalpha() for char in hey_bob):
        if hey_bob.strip().endswith("?"):
            if hey_bob == hey_bob.upper():
                return "Calm down, I know what I'm doing!"
            return "Sure."
        if hey_bob == hey_bob.upper():
            return "Whoa, chill out!"
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob.strip().endswith("?"):
        return "Sure."    
    return "Whatever."