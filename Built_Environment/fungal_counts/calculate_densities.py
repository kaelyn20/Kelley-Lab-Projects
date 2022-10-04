'''
Go through each file and extract sample indicator and density estimates for
each image. Add the densities of the same sample together and subtract the
density of the blanks.
'''

import os
import re

#get current working directory
path = os.getcwd()
folder = os.fsencode(path)

filenames = []

#read names of all the files in the path and add all csv files to filename list
for file in os.listdir(folder):
    filename = os.fsdecode(file)
    csv = re.search('\.csv$', filename)

    if csv:
        filenames.append(filename)

counts = {}
samples = []
blnk = 670.43606136311 #replace this with new number

#Go through each file and extract the counts
for f in filenames:
    fopen = open(f, 'r')
    fread = fopen.readlines()

    #For each line in the file, strip the white space and separate based on commas
    for line in fread:
        cols = line.strip()
        cols = cols.split(',')

        #extract sample indicator from the first column
        samp = re.match('W[0-9]_M[0-9]+', cols[0])
        if samp:
            name = samp.group()

        #samples.append(name)
        #change the variable type of cols[1] to a float so it's numeric
        cols[1] = float(cols[1])

        #if the dictonary already contains the sample, add the density to the
        #previous density. If not, set the value to the current density and
        #subtract the blank density
        if name in counts :
            counts[name] += cols[1]
        else :
            counts[name] = cols[1] - blnk

#print the keys and values for each item in the dictionary. If the value is
#negative, set it to 0.
for k, v in counts.items() :
    if v < 0 :
        v = 0
    print(k, v)

