
with open('rosalind_ini5.txt', 'U') as output:
    i = 0
    for line in output:
        line = line.strip()
        i+=1
        if i % 2 ==0:
            print line
        
        
