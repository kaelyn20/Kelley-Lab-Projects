'''
This script compares barcodes from the ITS and 16S barcodes and returns
the barcodes that are not repeated


'''
def compare(l1, l2) :
    unused = ""
    for el in l1 :
        if el in l2 :
            pass
        else :
           unused += el

    return unused

fopen = open("barcodes.csv", 'r')
fread = fopen.readlines()

its = []
S16 = []
for line in fread :
    cols = line.strip()
    cols = line.replace(" ", "")
    cols = cols.split(",")

    S16.append(cols[1])
    if cols[0] == '':
        pass
    else :
        its.append(cols[0])

fout = open("unused16s.txt", 'w')
fout.write(compare(S16, its))

fopen.close()
fout.close()
