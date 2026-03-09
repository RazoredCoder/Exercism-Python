'''Given a name and a number, your task is to produce a sentence using that name and that number as an ordinal numeral.'''
def line_up(name, number):
    '''Given a name and a number, your task is to produce a sentence using that name and that number as an ordinal numeral.
    :param name: str - name of a client
    :param number: int - number in the queue
    :return: str - a custom message for a client
    '''
    endings = ['th','st', 'nd', 'rd']
    try:
        if number > 10 and int(str(number)[-2]) == 1:
            raise IndexError
        return f'{name}, you are the {number}{endings[int(str(number)[-1])]} customer we serve today. Thank you!'
    except IndexError:
        return f'{name}, you are the {number}th customer we serve today. Thank you!'