class DeBruijn(object):
    """Debruign class object, creating kmer and self"""
    def __init__(self, kmer):
        """constructer of class DeBruijn"""
        self.kmer = kmer
        self.edge = set()
    def __str__(self):
        """print the contents of an object."""
        return '{0}'.format(self.kmer)
        
def DNA_extract():
    """ Extract DNA from sequences"""
    DNA_list=[]
    with open('rosalind_dbru.txt', 'U') as reader:
        for line in reader:
            line = line.strip()
            DNA_list.append(line)
    return DNA_list

def reverse_complement(DNA_list):
    """ Do reverse complement on the DNA sequences"""
    Rev_list = []
    rev_dict = {'A':'T', 'G':'C', 'C':'G', 'T': 'A'}
    for i in DNA_list:
        Rev_DNA=""
        for nucleotide in i:
            Rev_DNA += rev_dict[nucleotide]
            Reverse_DNA = Rev_DNA[::-1]
            
        Rev_list.append(Reverse_DNA)
    Final_list = DNA_list + Rev_list
    return Final_list
    
def kmers(DNA):
    """ get kmer of 1 less len(DNA)"""
    kmer_list=[]
    k = len(DNA)-1
    for i in range(k, len(DNA)+1):
        kmer_list.append(DNA[i-k:i])
    return kmer_list
    
def main():
    """main function for calling DeBruign code"""
    DNA_list = DNA_extract()
    Final_list = reverse_complement(DNA_list)
    Node_dict={}
    for DNA in Final_list:
        last_node = None
        for kmer in kmers(DNA):
            if kmer not in Node_dict:
                Node_dict[kmer] = DeBruijn(kmer)
            if last_node:
                last_node.edge.add(Node_dict[kmer])
            last_node = Node_dict[kmer]
    for kmer, node in sorted(Node_dict.iteritems()):
        for edge in node.edge:     
            print "({0}, {1})".format(kmer, edge)


if __name__ == '__main__':
    main()
