# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fread = fh.read()
print(fread.upper().rstrip())