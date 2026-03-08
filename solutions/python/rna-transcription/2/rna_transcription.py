'''Determine the RNA complement of a given DNA sequence.'''
def to_rna(dna_strand:str):
    '''Determine the RNA complement of a given DNA sequence.
    :param dna_strand: str - a strand of DNA sequence
    :return: str - a complement RNA sequence
    '''
    if len(dna_strand) < 1:
        return ''
    dna_list = list(dna_strand)
    complements = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for index, nucleotide in enumerate(dna_list):
        if nucleotide not in complements:
            continue
        dna_list[index] = complements[nucleotide]
    return ''.join(dna_list)