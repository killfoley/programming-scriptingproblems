#This program reads in a text file and returns
#the number of e's it contains.

import sys

with open(sys.argv[1], 'r') as f:
    read_data = f.read().replace('\n', '')
    
    c = read_data.count("e")

    print(c)