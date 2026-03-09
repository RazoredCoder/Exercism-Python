'''Calculate the Hamming distance between two DNA strands.'''
def distance(strand_a:str, strand_b:str):
    '''Calculate the Hamming distance between two DNA strands.
    :param strand_a: str - one strand of DNA for comparison
    :param strand_b: str - the other strand of DNA for comparison
    :return: int - the Hamming distance between two strands
    '''
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(0 if pair[0] == pair[1] else 1 for pair in zip(strand_a, strand_b))