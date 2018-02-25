#s = 'HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.'



with open('rosalind_ini3.txt', 'U') as output:
    number =[]
    for line in output:
        line = line.strip()
        if " " in line:
            line = line.split(" ")
            number.append(int(line[0]))
            number.append(int(line[1]))
            number.append(int(line[2]))
            number.append(int(line[3]))
        else:
            s = line
        
    print s[number[0]:number[1]+1], s[number[2]:number[3]+1]
