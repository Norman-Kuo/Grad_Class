DNA =""
k = 0

with open('rosalind_ba3a.txt' ,'U') as reader:
    for line in reader:
        line = line.strip()
        if line.isdigit() == True:
            k = int(line)
        else:
            DNA+=line

def kmers():
    for i in range(k, len(DNA)+1):
        print DNA[i-k:i]
