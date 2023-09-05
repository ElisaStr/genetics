import csv

data_file = ".\data\genetic_code.tsv"

RNAcode= {}

with open(data_file, "r", encoding="utf-8") as file:
    tsvreader = csv.reader(file, delimiter='\t')

    for row in tsvreader:
        RNAcode[row[0]] = [row[1], row[2], row[3]]

#print(RNAcode)

DNAcode = {}
for key, value in RNAcode.items():
    DNA_key = key.replace("U", "T")
    DNAcode[DNA_key] = value

#print(DNAcode)


def DNAsequence_to_aminoacid(DNA):

    DNAtriplets = [DNA[i:i+3] for i in range(0, len(DNA), 3)]
    print(DNAtriplets)

    aasequence = []
    for triplet in DNAtriplets:

        for key, value in DNAcode.items():
            if triplet == key:
                aasequence.append(value[0])
    aasequencejoined = "".join(aasequence)

    print(aasequencejoined)

DNAsequence_to_aminoacid("CTCCGCACTGCTCACTCCCGCGCAGTGAGGTTGGCACAGCCACCGCTCTGTGGCTCGCTTGGTTCCCTTAGTCCCGAGCGCTCGCCCACTGCAGATTCCTTTCCCGTGCAGACATGGCCT")


def RNAsequence_to_aminoacid(RNA):

    RNAtriplets = [RNA[i:i+3] for i in range(0, len(RNA), 3)]
    print(RNAtriplets)

    aasequence = []
    for triplet in RNAtriplets:

        for key, value in RNAcode.items():
            if triplet == key:
                aasequence.append(value[0])
    aasequencejoined = "".join(aasequence)

    print(aasequencejoined)

RNAsequence_to_aminoacid("CUCAUCGAUCGAACCUUGAGUUCAAGA")

def nucleotides_to_amicoacid(sequence):
    if sequence.find("U") ==True:
        print("This is a mRNA sequence")
        RNAsequence_to_aminoacid(sequence)
    elif sequence.find("T") == True:
        print("This is a DNA sequence")
        DNAsequence_to_aminoacid(sequence)
    else:
        print("This is no valid nucleotide sequence")


nucleotides_to_amicoacid("CTCCGCACTGCTCACTCCCGCGCAGTGAGGTTGGCACAGCCACCGCTCTGTGGCTCGCTTGGTTCCCTTAGTCCCGAGCGCTCGCCCACTGCAGATTCCTTTCCCGTGCAGACATGGCCT")

nucleotides_to_amicoacid("CUCAUCGAUCGAACCUUGAGUUCAAGAAGUUCGGGGCCAUUCGAUUAGCAGUGACCAGGGUUUACG")

nucleotides_to_amicoacid("123456789")