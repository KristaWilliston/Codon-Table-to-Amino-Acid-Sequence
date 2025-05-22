# Write a program that takes a codon table file (standard.code) and a file containing nucleotide sequence (anthrax_sasp.nuc) as command-line arguments, and outputs the amino-acid sequence.
# Modify the program to indicate whether or not the initial codon is consistent with the codon table's start codons.
# Use NCBI's taxonomy resource to look up and download the correct codon table for the anthrax bacterium. Re-run the program using the correct codon table.

# # Exercise 3
# use init dictionary for the "modify your program to indicate..." part

import sys
table = sys.argv[1]
anthrax = sys.argv[2]

table = open('standard.code')
data = {}
for l in table:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value    
table.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = (st[i] == 'M')

anthrax = open('anthrax.txt')
seq = ''.join(anthrax.read().split())
anthrax.close()
seqlen = len(seq)
aaseq = []
for i in range(0,seqlen,3):
    codon = seq[i:i+3]
    aa = codons[codon]
    aaseq.append(aa)
print(''.join(aaseq))


start_codon = seq[:3]
if init.get(start_codon):
    print("True")
else:
    print("False")
