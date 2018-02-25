#Problem 15

def counting_point_mutations():
    with open('rosalind_hamm.txt', 'U') as reader:
        DNA_list = []
        for line in reader:
            line = line.strip()
            DNA_list.append(line)

    count = 0
    for i in range(0, len(DNA_list[0])):
        if DNA_list[0][i] != DNA_list[1][i]:
            count +=1
    print count
            
