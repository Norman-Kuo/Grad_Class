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



protein = ""
with open('rosalind_mrna.txt', 'U') as output:
    for line in output:
        line = line.strip()
        protein +=line


product = 3 # (three stop codon)
for AA in protein:
    i=0
    for key in standard_code:
        if standard_code[key] == AA:
            i+=1
    product = product*i
print product % 1000000


