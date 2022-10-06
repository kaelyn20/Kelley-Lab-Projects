'''
split linker and primer
'''

fopen = open("primers_to_order.csv", 'r')
fread = fopen.readlines()

for line in fread :
    cols = line.strip()
    cols = line.replace(" ", "")
    cols = cols.split(",")

    string =cols[0] + cols[1] + cols[2]
    print(string.strip())
