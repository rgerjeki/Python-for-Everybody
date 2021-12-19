name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle: #reads through each line in .txt file
    if not line.startswith("From:"): #looks for "From:"
        continue
    elif line.startswith("From:"): #runs when finds "From:"
        emails = line.split() #splits line into words 
        del emails[0] #deleted "From:" from emails list
        for word in emails: #reads words in emails
            if word not in counts: #adds word in counts dict() if not yet in counts
                counts[word] = 1
            else:
                counts[word] += 1 #adds 1 to the value if key already in counts dict()
max_key = max(counts, key = counts.get) #gets key with the max value

all_values = counts.values()
max_value = max(all_values) #gets the max value
print(max_key, max_value)