import collections


def spliced_motif():
    fasta = collections.OrderedDict()
    with open('rosalind_sseq.txt', 'U') as multifasta:
        sequence = ""
        for row in multifasta:
            
            if row.startswith('>'):
                header = row.strip()
                sequence = ""
            else:
                sequence += row.strip()
            fasta[header] = sequence
    sequences = []
    for k, v in fasta.iteritems():
        sequences.append(v)
    index = 0
    answer = []
    previous_index = 0
    print sequences[0]
    print sequences[1]
    for nucleotide in sequences[1]:
        
        index = [pos for pos, char in enumerate(sequences[0]) if char == nucleotide]
        #print index
        #print index
        for i in index:
            #print i
            if i > previous_index:
                previous_index = i
                answer.append(str(i+1))
                #print answer
                break
        
    print ' '.join(answer)
