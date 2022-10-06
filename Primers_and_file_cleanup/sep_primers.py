primers = "16Sprimers1-3.csv"

fopen = open(primers, 'r')
fread = fopen.readlines()

for line in fread :
    cols = line.strip()
    cols = cols.split(",")

    print(cols[3][0:16])
