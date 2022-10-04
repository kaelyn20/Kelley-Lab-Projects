import os
import re

#get current working directory
path = os.getcwd()
folder = os.fsencode(path)

filenames = []

#read names of all the files in the path and add all csv files to filename list
for file in os.listdir(folder):
    filename = os.fsdecode(file)
    #print(filename)
    csv = re.search('\.csv$', filename)

    if csv:
        filenames.append(filename)

sum_cnts = 0
#samples = []

#for each blank file, add the density estimates
for f in filenames:
    fopen = open(f, 'r')
    fread = fopen.readlines()

    for line in fread:
        cols = line.strip()
        cols = cols.split(',')
        

        #convert cols[1] to a numeric value
        cols[1] = float(cols[1])
        sum_cnts += cols[1]

print(sum_cnts)
