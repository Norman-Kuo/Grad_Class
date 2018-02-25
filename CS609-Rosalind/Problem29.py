

def hpp():
    with open('rosalind_ba10b.txt', 'U') as reader:
        whole_list = []
        for row in reader:
            #print row.split()
            whole_list.append(row.split())


    to_sequence = whole_list[0][0]
    pre_sequence = whole_list[4][0]
    FromAx = whole_list[9][1]
    FromAy = whole_list[9][2]
    FromAz = whole_list[9][3]
    FromBx = whole_list[10][1]
    FromBy = whole_list[10][2]
    FromBz = whole_list[10][3]

    final=1
    previous_nucleotide = ""
    for number in range(len(to_sequence)):
        if pre_sequence[number] == "A":
            if to_sequence[number] == 'x':
                probability = float(FromAx)
            elif to_sequence[number] =='y':
                probability = float(FromAy)
            else:
                probability = float(FromAz)
        if pre_sequence[number] == "B":
            if to_sequence[number] == 'x':
                probability = float(FromBx)
            elif to_sequence[number] =='y':
                probability = float(FromBy)
            else:
                probability = float(FromBz)
        final *= probability
        
    print final
    

