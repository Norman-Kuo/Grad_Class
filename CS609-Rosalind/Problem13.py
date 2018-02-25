import re

standard_code = { "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
                      "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
                      "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
                      "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
                      "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
                      "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
                      "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
                      "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
                      "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
                      "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
                      "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
                      "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
                      "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}


for_DNA = ''
with open('rosalind_orf.txt', 'U') as output:
    for line in output:
        line = line.strip()
        if '>' not in line:
            for_DNA += line


rev_DNA = ''
for nucleotide in for_DNA:
    if nucleotide =='A':
        rev_DNA += 'T'
    elif nucleotide =='T':
        rev_DNA += 'A'
    elif nucleotide =='G':
        rev_DNA += 'C'
    elif nucleotide =='C':
        rev_DNA += 'G'
rev_DNA = rev_DNA[::-1]


for_RNA = ''
rev_RNA = ''
for nucleotide in for_DNA:
    if nucleotide == 'T':
        for_RNA += 'U'
    else:
        for_RNA += nucleotide

for nucleotide in rev_DNA:
    if nucleotide == 'T':
        rev_RNA += 'U'
    else:
        rev_RNA += nucleotide



rev_Protein = ""

forward_start = [m.start() for m in re.finditer('AUG', for_RNA)]
reverse_start = [m.start() for m in re.finditer('AUG', rev_RNA)]

ORF = {}

for i in forward_start:
    for_Protein = ""
    for k in range(i, len(for_RNA), 3):
        codon = for_RNA[k:k+3]
        if len(codon) ==3:
            protein = standard_code[codon]
            if protein != '*':
                for_Protein += protein
            else:
                for_Protein += protein
                break
    if '*' in for_Protein:
        ORF[for_Protein[0:-1]] = i

for i in reverse_start:
    rev_Protein = ""
    for k in range(i, len(rev_RNA), 3):
        codon = rev_RNA[k:k+3]
        if len(codon) ==3:
            protein = standard_code[codon]
            if protein != '*':
                rev_Protein += protein
            else:
                rev_Protein += protein
                break
    if '*' in rev_Protein:
        ORF[rev_Protein[0:-1]] = i

for k in ORF:
    print k

            
