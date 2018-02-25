DNA = ""
previous = ''
with open('rosalind_ba3b.txt', 'U') as reader:
    for line in reader:
        line = line.strip()
        if DNA == "":
            DNA +=line
        else:
            DNA += line[-1]
        
        
print DNA
