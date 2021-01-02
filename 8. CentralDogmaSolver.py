#3.2.2018
#Central Dogma Solver 5.4.0

'''Pseudocode: The program is designed to 'replicate', 'transcript', and 'translate' the DNA or mRNA sequence entered by the user. It finds the complentary base DNA
or RNA base (depending on the user's choice), stored in its dictionary, for the user's DNA squence. The program can also convert a mRNA squence into proteins.
it first divides up the sequence into codons, and then translates them into proteins. The program finally displays the information to the user.'''

Purpose = int(input('Are you trying to (1)find a complementary strand for a DNA sequence or (2)covert a mRNA strand into proteins? '))
if Purpose == 1:
    DNA_Complementary_Bases = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    RNA_Complementary_Bases = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}
    Letter_List = []
    DNA_Or_RNA = input('Do you want to find the DNA or RNA complemtary strand? ')
    DNA_Strand = input('Enter DNA strand sequence: ')
    for letters in DNA_Strand.replace(' ',''):
        if DNA_Or_RNA.upper() == 'DNA':
            Letter_List.append(DNA_Complementary_Bases[letters.upper()])
        elif DNA_Or_RNA.upper() == 'RNA':
            Letter_List.append(RNA_Complementary_Bases[letters.upper()])
            
    print(DNA_Or_RNA.upper(),'Stand:',"".join(Letter_List))
    print('With complementary DNA bases, adenine (A) binds with thymine (T) and vice versa, and guanine (G) binds with cytosine (C)and vice versa.')
    print('With complementary mRNA bases, adenine (A) binds with uracil (U), thymine (T) binds with adenine (A), and guanine (G) binds with cytosine (C) and vice versa.')

elif Purpose == 2:
    RNA_Complementary_Proteins = {'Phe':['UUU','UUC'],
                                  'Leu':['UUA','UUG','CUU','CUC','CUA','CUG'],
                                  'Ile':['AUU','AUC','AUA'],
                                  'Met(Start)': 'AUG',
                                  'Val':['GUU','GUC','GUA','GUG'],
                                  'Ser':['UCU','UCC','UCA','UCG','AGU','AGC'],
                                  'Pro':['CCU','CCC','CCA','CCG'],
                                  'Thr':['ACU','ACC','ACA','ACG'],
                                  'Ala':['GCU','GCC','GCA','GCG'],
                                  'Tyr':['UAU','UAC'],
                                  'Stop':['UAA','UAG','UGA'],
                                  'His':['CAU','CAC'],
                                  'Gin':['CAA','CAG'],
                                  'Asn':['AAU','AAC'],
                                  'Lys':['AAA','AAG'],
                                  'Asp':['GAU','GAA'],
                                  'Glu':['GAA','GAG'],
                                  'Cys':['UGU','UGC'],
                                  'Trp':'UGG',
                                  'Arg':['CGU','CGC','CGA','CGG','AGA','AGG'],
                                  'Gly':['GGU','GGC','GGA','GGG']}
    def reverse_lookup(d,v):
        for k in d:
            if d[k] == v:
                return k
            elif v in d[k]:
                return k
        raise LookupError()
    Protein_List = []
    mRNA_Strand = input('Enter mRNA strand sequence: ').replace(' ','')
    for i in mRNA_Strand:
        if i.upper() not in ['A','U','G','C']:
            mRNA_Strand = input('Invalid base, enter sequence again: ').replace(' ','')
    while len(mRNA_Strand)%3 != 0:
        mRNA_Strand = input('Invalid number of bases, enter sequence again: ').replace(' ','')
    Condon_List = []
    for i in range(0, len(mRNA_Strand), 3):
        Condon_List.append(mRNA_Strand[i:i+3])
    for codons in Condon_List:
        Protein_List.append(reverse_lookup(RNA_Complementary_Proteins,codons.upper())) 
    print('Proteins:',", ".join(Protein_List))
