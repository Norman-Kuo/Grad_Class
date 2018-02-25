def file_parse():
    files = []
    with open('rosalind_ba10c.txt', 'U') as inputfile:
        for row in inputfile:
            row = row.strip()
            files.append(row)
    sequences = files[0]
    observe = files[2].split()
    observations = []
    states = files[4].split()
    start_probability = {}
    transition_probability = {}
    emission_probability = {}
    matrix = []
    for nucleotide in sequences:
        observations.append(nucleotide)
        
    for i in states:
        start_probability[i] = 0.5
    m = len(states)
    n = len(observe)
    for line in files[7:]:
        
        for number in line.split():
            try:
                number = float(number)
            except:
                pass
            if type(number) == float:
                matrix.append(number)
    trans= matrix[0:m*m]
    emiss= matrix[m*m:]

    for i in states:
        intermediate = {}
        for j in states:
            intermediate[j] = trans[0]
            trans.pop(0)
        transition_probability[i]=intermediate

    for i in states:
        intermediate = {}
        for j in observe:
            intermediate[j]=emiss[0]
            emiss.pop(0)
        emission_probability[i]=intermediate    
    return observations, states, start_probability, transition_probability, emission_probability


### The following code is retrieved by https://github.com/llrs/Viterbi/blob/master/Viterbi.py with minor modification ###
### Author: Lluis
### Date:  Mar 19, 2014 (Access on Dec 16, 2017)
### Title of Program/source code: Viterbi.py
### Code version: Not state
### Type: Python source code for solving Rosalind problem: Implement the Viterbi Algorithm For SDSU CS609 homework problem
### Availability: https://github.com/llrs/Viterbi/blob/master/Viterbi.py


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:

            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        path = newpath

    (prob, state) = max((V[t][y], y) for y in states)
    final = ""
    for i in path[state]:
        final+=i
    
    print final

def main():
    observations, states, start_probability, transition_probability, emission_probability = file_parse()
    viterbi(observations, states, start_probability, transition_probability, emission_probability)

if __name__=='__main__':
    main()
