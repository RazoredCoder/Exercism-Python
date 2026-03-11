'''Calculate the square root of a given number.'''
def square_root(number:int):
    for root in range(number + 1):
        if root * root == number:
            return root
    return None