#This program reads in a text file and returns
#the number of e's it contains.

with open("input") as f:
    read_data = f.read()

    c = f.count(e)

    print({} .format(c))