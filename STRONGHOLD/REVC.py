seq = input()
compl_nucl = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
compl_seq = ''
for i in reversed(seq):
    compl_seq += compl_nucl[i]

print(compl_seq)