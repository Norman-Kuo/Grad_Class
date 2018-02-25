import collections
import decimal


def distance_matrix():
    with open('rosalind_pdst.txt' ,'U') as multifasta:
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



    answer = ""
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            score = decimal.Decimal('0.00000')
            for k in range(len(sequences[i])):
                if sequences[i][k] != sequences[j][k]:
                    score += decimal.Decimal('1.00000')
            final_score= "%0.5f" % (score/len(sequences[i]))
            answer += str(final_score) + "\t"
        answer += "\n"
    print answer
                    
    
