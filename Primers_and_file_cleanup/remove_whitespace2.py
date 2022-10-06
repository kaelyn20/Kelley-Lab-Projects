import re

fopen = open("primers.txt", 'r')
fread = fopen.readlines()

for line in fread :
    print(line.replace(" ", "").strip())

fopen.close()
