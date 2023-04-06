import re


fopen = open("itstaxatable.tsv", 'r')
fread = fopen.readlines()

newline = ""

for line in fread:
    line = line.replace(";", "\t")
    line = re.sub("[a-z]__", "", line)
    line = re.sub("__", "", line)
    newline += line


fout = open("clean_ITStable.tsv", 'w')
fout.write(newline)


fopen.close()
