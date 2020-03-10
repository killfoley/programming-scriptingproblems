#This program reads in a text file and returns
#the number of e's it contains.

with open("moby-dick.txt", 'r') as f:
    read_data = f.read().replace('\n', '')
    
    c = read_data.count("e")

    print(c)