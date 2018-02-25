#DNA = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'


with open("rosalind_dna.txt" ,'U') as dataset:
    DNA = ""
    for line in dataset:
        line = line.strip()
        DNA += line

A = 0
T = 0
C = 0
G = 0
for nucleotide in DNA:
    if nucleotide =='A':
        A+=1
    elif nucleotide =='T':
        T+=1
    elif nucleotide =='G':
        G+=1
    elif nucleotide =='C':
        C+=1

print A, C, G, T
