

for_DNA = ''
with open('rosalind_ba1c.txt', 'U') as output:
    for line in output:
        line = line.strip()
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

print rev_DNA
