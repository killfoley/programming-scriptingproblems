#This program reads in a text file and returns
#the number of e's it contains.

#reference to filename import from command line
#https://stackoverflow.com/questions/7439145/i-want-to-read-in-a-file-from-the-command-line-in-python

import sys

with open(sys.argv[1], 'r') as f:
    read_data = f.read().replace('\n', '')
    
    c = read_data.count("e")

    print(c)