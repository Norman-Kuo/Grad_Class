import numpy as np

def edit_distance_alignment():
    with open('rosalind_edta.txt' ,'U') as multifasta:
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
    #print sequences
    if len(sequences[0]) > len(sequences[1]):
        long_seq = sequences[0]
        short_seq = sequences[1]
    else:
        long_seq = sequences[1]
        short_seq = sequences[0]

    m = len(long_seq)
    n = len(short_seq)
    zero_matrix = np.zeros(((m+1, n+1)))
    direction_matrix = np.zeros(((m+1, n+1)))

    for i in range(m+1):
        zero_matrix[i][0] = i
    for j in range(n+1):
        zero_matrix[0][j] = j
   # print zero_matrix

    for i in range(1, m+1):
        for j in range(1, n+1):
            if long_seq[i-1] == short_seq[j-1]:
                number = 0
            else:
                number =1
            zero_matrix[i][j]=min(zero_matrix[i-1][j]+1, zero_matrix[i][j-1]+1, zero_matrix[i-1][j-1]+ number)
            if min(zero_matrix[i-1][j]+1, zero_matrix[i][j-1]+1, zero_matrix[i-1][j-1]+ number) == zero_matrix[i-1][j]+1:
                direction_matrix[i][j] = 2
            elif min(zero_matrix[i-1][j]+1, zero_matrix[i][j-1]+1, zero_matrix[i-1][j-1]+ number) == zero_matrix[i][j-1]+1:
                direction_matrix[i][j] = 3
            else:
                direction_matrix[i][j] = 1
                

    
    #print zero_matrix
    #print direction_matrix
    print zero_matrix[m, n]

    process_seq1 =long_seq
    process_seq2 =short_seq 
    sequence1= ""
    sequence2 = ""
    i = m
    j = n
    while i > 0 and j > 0:
        #print i, j
        if direction_matrix[i][j] == 1:
            sequence1 =  process_seq1[-1] + sequence1
            sequence2 =  process_seq2[-1] + sequence2
            process_seq1= process_seq1[:-1]
            process_seq2= process_seq2[:-1]
            i-=1
            j-=1
        elif direction_matrix[i][j] == 2:
            sequence1 =  process_seq1[-1] + sequence1
            sequence2 =  '-' + sequence2
            process_seq1= process_seq1[:-1]
            i-=1
        elif direction_matrix[i][j] == 3:
            sequence2 =  process_seq2[-1] + sequence2
            sequence1 =  '-' + sequence1
            process_seq2= process_seq2[:-1]
            j-=1

    print sequence1
    print sequence2
