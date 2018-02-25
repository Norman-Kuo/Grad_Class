with open('rosalind_tran.txt' ,'U') as multifasta:
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


transversion = 0
transition = 0


for i in range(len(sequences[0])):
    if sequences[0][i] == sequences[1][i]:
        continue
    else:
        if sequences[0][i] =='A':
            if sequences[1][i] =='G':
                transition +=1
            elif sequences[1][i] =='T':
                transversion +=1
            elif sequences[1][i] =='C':
                transversion +=1
        elif sequences[0][i] =='G':
            if sequences[1][i] =='A':
                transition +=1
            elif sequences[1][i] =='T':
                transversion +=1
            elif sequences[1][i] =='C':
                transversion +=1
        elif sequences[0][i] =='T':
            if sequences[1][i] =='A':
                transversion +=1
            elif sequences[1][i] =='G':
                transversion +=1
            elif sequences[1][i] =='C':
                transition +=1
        elif sequences[0][i] =='C':
            if sequences[1][i] =='A':
                transversion +=1
            elif sequences[1][i] =='T':
                transition +=1
            elif sequences[1][i] =='G':
                transversion +=1


print float(transition)/float(transversion)
