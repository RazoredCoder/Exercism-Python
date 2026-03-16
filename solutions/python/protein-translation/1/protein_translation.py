def proteins(strand:str):
    if len(strand) < 1: return None
    strands = []
    for increment in range(0, len(strand), 3):
        strands.append(strand[increment:3+increment])
    protein_dict = {('AUG',): 'Methionine',
                    ('UUU', 'UUC'): 'Phenylalanine',
                    ('UUA', 'UUG'): 'Leucine',
                    ('UCU', 'UCC', 'UCA', 'UCG'): 'Serine',
                    ('UAU', 'UAC'): 'Tyrosine',
                    ('UGU', 'UGC'): 'Cysteine',
                    ('UGG',): 'Tryptophan',
                    ('UAA', 'UAG', 'UGA'): 'STOP',
                    }
    translation = []
    for codon in strands:
        amino_acid = next(val for key, val in protein_dict.items() if codon in key)
        if amino_acid == 'STOP':
            break
        translation.append(amino_acid)
    return translation