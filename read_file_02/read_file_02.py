# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
lcount = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    elif line.startswith("X-DSPAM-Confidence:"):
        lcount = lcount + 1
        fpoint = line[20:]
        x = float(fpoint.rstrip())
        total = total + x
        #print(x)
        
    #print(line.rstrip())
average = total / lcount
#print(total)
#print(lcount)
print("Average spam confidence:", average)