import itertools


def permutation(k):
    number_list = []
    for i in range(1, k+1):
        number_list.append(i)
    print len(list(itertools.permutations(number_list)))
    for i in (itertools.permutations(number_list)):
        tuple_list=[]
        for j in i:
            tuple_list.append(str(j))
        print ' '.join(tuple_list)
