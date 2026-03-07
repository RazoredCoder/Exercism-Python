'''Given a string the program should check if the provided string is a valid ISBN-10.'''
def is_valid(isbn:str):
    '''Given a string the program should check if the provided string is a valid ISBN-10.
    :param isbn: str - ISBN number to check
    :return: bool - is valid or not'''
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    weight = 10
    isbn_sum = 0
    for char in isbn:
        try:
            num = int(char)
        except ValueError:  
            if char == 'X' and isbn.index(char) == 9:
                num = 10
            else: return False
        isbn_sum += num * weight
        weight -= 1
    return isbn_sum % 11 == 0