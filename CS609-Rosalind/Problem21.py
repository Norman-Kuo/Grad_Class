import collections

def SuffixArray():
    string_text = ""
    with open('rosalind_ba9g.txt', 'U') as filehandler:
        for line in filehandler:
            line = line.strip()
            string_text+=line
    string_dict = {}
    i = 0
    while len(string_text)>0:
        string_dict[string_text] = i
        string_text = string_text[1:]
        i +=1
    sort_string_dict = collections.OrderedDict(sorted(string_dict.items()))
    index_list= []
    for k, v in sort_string_dict.iteritems():
        index_list.append(str(v))
    print ', '.join(index_list)

if __name__=='__main__':
    SuffixArray()
    
        
    
