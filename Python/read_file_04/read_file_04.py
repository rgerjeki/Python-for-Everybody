fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0 #initializes counter
for line in fh: #reads through each line in .txt file
    if not line.startswith("From:"): #looks for "From:"
        continue
    elif line.startswith("From:"): #runs when finds "From:"
        count = count + 1 #adds 1 to count
        emails = line.split() #splits line into words 
        del emails[0] #deleted "From:" from emails list
        print(emails[0]) #prints out email without list format ([''])
print("There were", count, "lines in the file with From as the first word")