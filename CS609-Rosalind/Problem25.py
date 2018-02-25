import collections

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

def RNA_splicing():
    with open('rosalind_splc.txt', 'U') as multifasta:
        seq_dict = collections.OrderedDict()
        for line in multifasta:
            line = line.strip()
            if line.startswith('>'):
                header = line
                sequence = ''
            else:
                sequence += line
                seq_dict[header] = sequence
    sequences = []
    for k, v in seq_dict.iteritems():
        sequences.append(v)
    main_seq = sequences[0]
    #print sequences[0]
    for i in range(1, len(sequences)):
        main_seq = main_seq.replace(sequences[i], "")
        
    #print main_seq
    RNA= ""
    for nucleotide in main_seq:
        if nucleotide == "T":
            RNA += "U"
        else:
            RNA += nucleotide
    Protein = ""
    for i in range(0, len(RNA), 3):
        codon = RNA[i:i+3]
        Protein += standard_code[codon]
    print Protein[:-1]
    
    
