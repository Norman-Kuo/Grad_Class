

def mendel():
    with open('rosalind_iprb.txt', 'U') as inputfile:
        for row in inputfile:
            row = row.strip()
            row = row.split(' ')
            k, m, n = float(row[0]), float(row[1]), float(row[2])
    total = k+m+n
    AA = ((k/total)*((k-1)/(total-1))*1) + ((k/total)*((m)/(total-1))*1) + ((k/total)*((n)/(total-1))*1)
    Aa = ((m/total)*((k)/(total-1))*1) + ((m/total)*((m-1)/(total-1))*0.75) + ((m/total)*((n)/(total-1))*0.5)
    aa = ((n/total)*((k)/(total-1))*1) + ((n/total)*((m)/(total-1))*0.5) + ((n/total)*((n-1)/(total-1))*0)
    print AA + Aa + aa
