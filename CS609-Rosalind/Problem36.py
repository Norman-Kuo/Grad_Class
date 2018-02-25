from Bio.SubsMat.MatrixInfo import pam250
import numpy as np

def local_alignment():

    with open('rosalind_loca.txt' ,'U') as multifasta:
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
    #print m, n
    zero_matrix = np.zeros(((m+1, n+1)))
    direction_matrix = np.zeros(((m+1, n+1)))
    print zero_matrix

    for i in range(m+1):
        zero_matrix[i][0] = 0
    for j in range(n+1):
        zero_matrix[0][j] = 0
    #print zero_matrix
    #print pam250
    best_match = 0
    coordinate = (0,0)
    for i in range(1, m+1):
        for j in range(1, n+1):
            try:
                number = pam250[(long_seq[i-1],short_seq[j-1])]
            except:
                number = pam250[(short_seq[j-1],long_seq[i-1])]
            #zero_matrix[i][j]=max(zero_matrix[i-1][j]-5, zero_matrix[i][j-1]-5, zero_matrix[i-1][j-1]+ number, 0)
            if max(zero_matrix[i-1][j]-5, zero_matrix[i][j-1]-5, zero_matrix[i-1][j-1]+ number, 0) == zero_matrix[i-1][j-1]+ number:
                zero_matrix[i][j] = zero_matrix[i-1][j-1]+ number
                direction_matrix[i][j] = 1
            elif max(zero_matrix[i-1][j]-5, zero_matrix[i][j-1]-5, zero_matrix[i-1][j-1]+ number, 0) == zero_matrix[i][j-1]-5 and zero_matrix[i][j-1]-5 != zero_matrix[i-1][j]-5 and zero_matrix[i][j-1]-5 != zero_matrix[i-1][j-1]+ number:
                zero_matrix[i][j] = zero_matrix[i][j-1]-5
                direction_matrix[i][j] = 3
            elif max(zero_matrix[i-1][j]-5, zero_matrix[i][j-1]-5, zero_matrix[i-1][j-1]+ number, 0) == zero_matrix[i-1][j]-5 and zero_matrix[i-1][j]-5 != zero_matrix[i][j-1]-5 and zero_matrix[i-1][j]-5 != zero_matrix[i-1][j-1]+ number:
                zero_matrix[i][j] =  zero_matrix[i-1][j]-5
                direction_matrix[i][j] = 2
            else:
                zero_matrix[i][j] = 0
                direction_matrix[i][j] = 0
            if zero_matrix[i][j] > best_match:
                best_match  = zero_matrix[i][j]
                coordinate = (i,j)
    #print zero_matrix
    print int(best_match)
    print coordinate
    p = coordinate[0]
    q = coordinate[1]
    #print long_seq[p-1], short_seq[q-1]
    align_long = ""
    align_short = ""

    #print long_seq
    #print short_seq
    while direction_matrix[p][q] != 0:
        if direction_matrix[p][q] == 1:
            align_long = long_seq[p-1] + align_long  
            align_short = short_seq[q-1] + align_short 
            p-=1
            q-=1
        elif direction_matrix[p][q] == 3:
            align_short = short_seq[q-1] + align_short 
            #align_long = '-' + align_long  
            q-=1
        elif direction_matrix[p][q] == 2:
            align_long = long_seq[p-1] + align_long  
            #align_short = '-' + align_short 
            p-=1


        #print p, q
    print align_long
    print align_short
            
            

