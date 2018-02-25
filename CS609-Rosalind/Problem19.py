import collections

def multifasta():
    with open('rosalind_lcsm.txt' ,'U') as multifasta:
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
    
    #i = len(sequences[0])
    k=0
    #print sequences
    first_sequence = sequences[0]
    #print first_sequence
    total_length = len(first_sequence)
    while total_length >0:
        
        start = len(first_sequence) - total_length    
        for i in range(start):
            string = first_sequence[i:i+total_length+1]
            match = []
            for j in range(1, len(sequences)):
                if string in sequences[j]:
                    match.append('yes')
                else:
                    match.append('no')
            if 'no' not in match:
                print string
                break

        total_length -=1
        
        
        
    
