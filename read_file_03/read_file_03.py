fname = input("Enter file name: ")
fh = open(fname)
lst = list()
newlist = list() #create new list to get rid of duplicates

for line in fh:
    line = line.rstrip()
    lst = lst + line.split()
    lst.sort()
for word in lst:
    if word not in newlist: #reads through empty list
        newlist.append(word) #adds words only if not already in newlist
print(newlist)
    