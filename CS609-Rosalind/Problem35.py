from Bio.SubsMat.MatrixInfo import blosum62
import numpy as np

def global_alignment():
    with open('rosalind_glob.txt' ,'U') as multifasta:
        seq_dict = {}
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
    if len(sequences[0]) > len(sequences[1]):
        long_seq = sequences[0]
        short_seq = sequences[1]
    else:
        long_seq = sequences[1]
        short_seq = sequences[0]
    print long_seq
    print short_seq
    m = len(long_seq)
    n = len(short_seq)
    zero_matrix = np.zeros(((m+1, n+1)))
    #print zero_matrix

    for i in range(m+1):
        zero_matrix[i][0] = i*-5
    for j in range(n+1):
        zero_matrix[0][j] = j*-5
    #print zero_matrix
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            try:
                number = blosum62[(long_seq[i-1],short_seq[j-1])]
            except:
                number = blosum62[(short_seq[j-1],long_seq[i-1])]
            zero_matrix[i][j]=max(zero_matrix[i-1][j]-5, zero_matrix[i][j-1]-5, zero_matrix[i-1][j-1]+ number)
    print int(zero_matrix[-1, -1])
