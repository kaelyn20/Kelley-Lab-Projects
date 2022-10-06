sam_list = []

fopen = open("16S_PCR_Placement.csv", 'r')
fread = fopen.readlines()

for line in fread :
    cols = line.strip()
    cols = line.replace(" ", "")
    cols = cols.split(",")

    for i in range(0, len(cols)) :
        if cols[i] not in sam_list :
            sam_list.append(cols[i])

s_list = sorted(sam_list)

for sam in s_list :
    print(sam)
'''
for key in sam_dict :
    print(key)
if sam_dict[key] > 1 :
        print(key)
'''

