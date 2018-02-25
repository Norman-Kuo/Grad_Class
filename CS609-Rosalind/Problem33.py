import re
import urllib2

def protein_motif():
    N_glycosylation = '(?=[N][^P][ST][^P])'
        
    p = re.compile(N_glycosylation)

    
    with open('rosalind_mprt.txt', 'U') as uniprot_ids:
        for uniprot_id in uniprot_ids:
            sequence = ""
            uniprot_id = uniprot_id.strip()
            http = 'http://www.uniprot.org/uniprot/'+uniprot_id +'.fasta'
            fasta = urllib2.urlopen(http).read().split('\n')
            for sequences in fasta:
                if not sequences.startswith('>'):
                    sequence += sequences.strip()
            #print uniprot_id
    
            match = [item.start()+1 for item in p.finditer(sequence)]
            if match !=[]:
                print uniprot_id
                print ' '.join(map(str, match))
                
            
            
