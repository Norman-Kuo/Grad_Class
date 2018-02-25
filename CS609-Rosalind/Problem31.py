

def Conditions_and_Loops():
    with open('rosalind_ini4.txt','U') as reader:
        for row in reader:
            first = int(row.split()[0])
            second = int(row.split()[1])
    sumation = 0
    for i in range(first, second):
        if i%2 ==1:
            sumation += i
    print sumation
            


