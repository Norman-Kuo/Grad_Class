import itertools


def permutation(k):
    number_list = []
    for i in range(1, k+1):
        number_list.append(i)

    neg_number_list = []
    for j in number_list:
        neg_number_list.append(-j)
    all_number_list = number_list + neg_number_list


    Total_list=[]
    for tuple_list in (itertools.permutations(all_number_list, k)):
        real_list = []
        for i in tuple_list:
            if abs(i) not in real_list:
                real_list.append(abs(i))
        if len(real_list) ==k:
            Total_list.append(list(tuple_list))
        

    print len(Total_list)
    for i in Total_list:
        print ' '.join(str(j) for j in i)
