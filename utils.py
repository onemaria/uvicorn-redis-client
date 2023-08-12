
def transcribe_dna_to_rna(dna_sequence: str):
    uppercase_dna_sequence = dna_sequence.upper()
    dna_nucleotides = ['A', 'C', 'G', 'T']

    for nucleotides in dna_sequence:
        if nucleotides not in dna_nucleotides:
            return "The sequence contains a non nucleotide. Please check and insert again a correct sequence"

    transcription_dict = {"A": "U", "T": "A", "G": "C", "C": "G"}
    rna_sequence = "".join(transcription_dict[base] for base in uppercase_dna_sequence)

    return rna_sequence

def get_mrna_from_rna(rna_sequence: str):
    reverse_transcription_dict = {"U": "A", "A": "U", "C": "G", "G": "C"}
    mrna_sequence = "".join(reverse_transcription_dict[base] for base in rna_sequence)
    return mrna_sequence

def translate_mrna_to_amino_acids(mrna_sequence: str):
    nucleotides = ['A', 'C', 'G', 'U']
    # reverse_transcription_dict = {"U": "A", "A": "U", "C": "G", "G": "C"}
    mrna_sequence = mrna_sequence.upper()

    # mrna_sequence = "".join(reverse_transcription_dict[base] for base in rna_sequence)

    codons = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
        "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    }

    for nucleotide in mrna_sequence:
        if nucleotide not in nucleotides:
            return "The sequence contains a non nucleotide. Please check and insert again a correct sequence"
    mrna_sequence = mrna_sequence[:len(mrna_sequence) - len(mrna_sequence) % 3]

    codon_triplets = [mrna_sequence[i:i+3] for i in range(0, len(mrna_sequence), 3)]
    amino_acids = []

    for codon in codon_triplets:
        if codon in codons:
            amino_acid = codons[codon]
            if amino_acid == "*":
                break  # Stop translation on encountering a stop codon
            amino_acids.append(amino_acid)

    return "".join(amino_acids)

    # mrna_sequence = mrna_sequence[:len(mrna_sequence) - len(mrna_sequence) % 3]
    #
    # codon_triplets = [mrna_sequence[i:i+3] for i in range(0, len(mrna_sequence), 3)]
    # amino_acids = [codons[codon] for codon in codon_triplets]
    #
    # return "".join(amino_acids)


