DNA = ''

RNA = ""


with open('rosalind_rna.txt', 'U') as output:
    for line in output:
        line=line.strip()
        DNA += line

#print DNA
        
for nucleotide in DNA:
    if nucleotide == 'T':
        RNA += 'U'
    else:
        RNA += nucleotide

print RNA
