'''Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.'''
def steps(number:int):
    '''Given a positive integer, return the number of steps it takes to reach 1 according to the rules of the Collatz Conjecture.
    :param number:int - a positive integer
    :return:int = number of steps to achieve 1
    '''
    if number is not int and number <= 0:
        raise ValueError("Only positive integers are allowed")
    steps_num = 0
    num_float = float(number)
    while num_float > 1:
        if int(num_float) % 2 == 0:
            num_float /= 2
        else:
            num_float = num_float*3 + 1
        steps_num += 1
    if int(num_float) == 1:
        return steps_num
    return None