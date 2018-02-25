
def bwt():
    string_text=[]
    nucleotide_dict={}
    with open('test.txt', 'U') as filehandler:
        for line in filehandler:
            line=line.strip()
            for nucleotide in line:
                if nucleotide not in nucleotide_dict:
                    nucleotide_dict[nucleotide]=1
                else:
                    nucleotide_dict[nucleotide] = nucleotide_dict[nucleotide]+1
                string_text.append((nucleotide,nucleotide_dict[nucleotide]))
        
    print string_text
    sort_string_text = sorted(string_text)
    print sort_string_text

    position_dict = {}
    for i in range(len(sort_string_text)):
        position_dict[sort_string_text[i]]=string_text[i]
    #print position_dict
    i = len(sort_string_text)
    final_string = ""
    key = ('$', 1)
    #print key[0]
    while i > 0:
        final_string = key[0] + final_string
        key = position_dict[key]
        i-=1
    print final_string
    
        

if __name__=='__main__':
    bwt()
