'''Determine whether a given number is perfect, abundant or deficient'''
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if type(number) is not int or number <= 0:
        raise ValueError('Classification is only possible for positive integers.')
    
    aliquot_sum = sum(divisor for divisor in range(1, number) if number % divisor == 0)

    if aliquot_sum == number:
        return 'perfect'
    if aliquot_sum > number:
        return 'abundant'
    if aliquot_sum < number:
        return 'deficient'