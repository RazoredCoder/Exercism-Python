'''Calculate the number of grains of wheat on a chessboard.
'''
def square(number:int):
    '''Calculate the number of grains on a given square'''
    if (1 <= number <= 64) is not True:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    '''Calculate the total number of grains on the chessboard'''
    return sum(square(sq) for sq in range (1, 65))