#Problem 16
import re

def Finding_motif():
    with open('rosalind_subs.txt', 'U') as reader:
        DNA_list = []
        for line in reader:
            line = line.strip()
            DNA_list.append(line)
    output_list = [i for i in range(len(DNA_list[0])) if DNA_list[0].startswith(DNA_list[1], i)]
    new_list = [x+1 for x in output_list]
    print new_list
    final_list = map(str, new_list)
    

    #print ' '.join(final_list)
        
