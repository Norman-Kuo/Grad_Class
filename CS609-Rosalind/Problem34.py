import collections 
from Bio.Seq import Seq


def error_correction():
    read_list = []
    with open('rosalind_corr.txt', 'U') as reads:
        for line in reads:
            line = line.strip()
            if not line.startswith('>'):
                read_list.append(line)
    correct_list = []
    incorrect_list = []
    for read in read_list:
        if read_list.count(read) >1 or Seq(read).reverse_complement() in read_list:
            correct_list.append(read)
    for read in read_list:
        if read not in correct_list:
            incorrect_list.append(read)
    
    #print incorrect_list

    final_list = set()
    for incorrect_read in incorrect_list:
        for correct_read in correct_list:
            count = 0
            rev_count = 0

            for letter1, letter2 in zip(correct_read, incorrect_read):
                if letter1 != letter2:
                    count+=1
            if count ==1:
                final_list.add(incorrect_read + '->' + correct_read)

            for revletter1, revletter2 in zip(incorrect_read, Seq(correct_read).reverse_complement()):
                #print incorrect_read, Seq(correct_read).reverse_complement()
                if revletter1 != revletter2:
                    rev_count +=1
            if rev_count ==1:
                final_list.add(incorrect_read + '->' + str(Seq(correct_read).reverse_complement()))
    for reads in final_list:
        print reads
