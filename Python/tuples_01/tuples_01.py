name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle: #reads through each line in .txt file
    if not line.startswith("From"): #looks for "From"
        continue
    elif line.startswith("From"): #runs when finds "From"
        time = line.split() #splits line into words 
        del time[0:5] #deletes words/numbers up to time
        del time[1:] #deletes words/numbers after time
        for line in time: 
            hour = line.split(":") #splits by ":"
            del hour[1:] #deletes words/numbers after hour
            #print(hour)
            for word in hour: #reads numbers in hour
                if word not in counts: #adds hour in counts dict() if not yet in counts
                    counts[word] = 1
                    #print(counts)
                else:
                    counts[word] += 1 #adds 1 to the value if key already in counts dict()
                    #print(counts)
lst = list() #creates list to add dict() values to
for key, val in list(counts.items()): 
    lst.append((key, val)) #appends key and value to our list

lst.sort(reverse=False) #reverses order (smallest value to largest value)

for key, value in lst: #reads through our list
    print(key, value) #prints out each line in our list (key value)
