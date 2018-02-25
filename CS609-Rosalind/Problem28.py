

def hmm():
    with open('rosalind_ba10a.txt', 'U') as reader:
        whole_list = []
        for row in reader:
            whole_list.append(row.split())

    sequence = whole_list[0][0]
    FromAA = whole_list[5][1]
    FromAB = whole_list[5][2]
    FromBA = whole_list[6][1]
    FromBB = whole_list[6][2]
    probability = 1
    previous_nucleotide = ""
    for nucleotide in sequence:
        if previous_nucleotide == "":
            previous = 0.5
        else:
            if previous_nucleotide == "A":
                if nucleotide =="A":
                    previous = float(FromAA)
                else:
                    previous = float(FromAB)
            else:
                if nucleotide =="A":
                    previous = float(FromBA)
                else:
                    previous = float(FromBB)
        probability *=previous
        previous_nucleotide = nucleotide
    print probability
    
