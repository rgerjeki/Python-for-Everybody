import re
lst = list() #new list

name = input("Enter File:")
if len(name) < 1:
    name = "actual.txt"
open_text = open(name) #opens text file
for line in open_text:
    line = line.rstrip() #strips whitespace from the right
    x = re.findall('[0-9]+', line) #finds all numbers in lines with numbers
    #if len(x) > 0:    #Used to see str list previous
        #print(x)
    for value in x:
        lst.append(value) #adds all str values into one list
    for i in range(0, len(lst)): #searches through lst and turns each str to int
        lst[i] = int(lst[i])
print(sum(lst)) #returns sum of all int values in list