#s = 'We tried list and we tried dicts also we tried Zen'


with open('rosalind_ini6.txt', 'U') as output:
    s = ''
    for line in output:
        line=line.strip()
        s += line
    s_list = s.split(' ')
    word_dict = {}

    for i in s_list:
        number = s_list.count(i)
        word_dict[i] = number

    for k, v in word_dict.iteritems():
        print k, v
