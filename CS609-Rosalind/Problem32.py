

def Fibonacci_Rabbit():
    with open('rosalind_fibd.txt','U') as inputfile:
        for row in inputfile:
            m = int(row.split()[0])
            n = int(row.split()[1])

    life_span = []
    for month in xrange(n):
        life_span.append(0)
    life_span[0] = 1

    for month in xrange(1, m):
        birth = 0
        for i in reversed(xrange(1, n)):
            birth += life_span[i]
            life_span[i] = life_span[i-1]
        life_span[0] = birth
        print life_span
    print sum(life_span)
        
    
