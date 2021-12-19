
# Python for Everybody

Python projects assigned by [Dr. Charles Severance](https://www.py4e.com/) in his Python for everybody: Coursera course.


## Dictionaries 
[dict_01.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/dict_01)

``` python
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
```
## Compute Pay 
[ex_18.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/ex_18)

``` python
pay = 0
def computepay(h, r):
    return pay

hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
if h <= 40:
    pay = h * r
else:
    pay = 40 * r 
    h = h - 40
    r = r * 1.5
    pay = pay + h * r
p = computepay(h, r)
print("Pay", p)
```

## Smallest & Largest 
[ex_18_02.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/ex_18_02)

``` python
largest = None
smallest = None
y = True
yes_no = ""


def Ext(x):
    x = input("Would you like to enter another number? ('y', 'n'): ")
    
    if x == "y": #continues while loop
        y = True
    elif x == "n":
        print("Maximum is", largest) #output largest number
        print("Minimum is", smallest) #output smalles number
        exit() #closes program
    else: #input has to be 'y' or 'n'
        print("Invalid Input")
        Ext(x)

while y == True:
    try:
        num = int(input("Enter a number in between (-100 -> 1000): ")) #enter numbers
    except ValueError: #prints invalid if input is not int value
        print("Invalid Input")
        continue
    if num > 1000 or num < -100: #setting input boundries
        print("Invalid Input") #prints invalid if not within boundries
        continue
      
    for value in range(-101, num): #allows numbers below 0 to be read
        if smallest == None and largest == None: #starting numbers added to smallest and largest
            smallest = num
            largest = num
        elif num < smallest: #makes numbers following first number smallest if num < smallest
            smallest = num
        elif num > largest: #makes numbers following first number largest if num > largest
            largest = num 
    
    Ext(yes_no) #calls Ext function
```

## Grades: Decimal to Letter 
[ex_grades.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/ex_grades)

``` python
score = input("Enter grade in decimal form: ")
try:
    s = float(score)
except:
    print("Error, please enter numeric input")
    quit()

if s > 1.0:
    print("Error, out of range")
    quit()
elif s < 0.0:
    print("Error, out of range")
    quit()
elif s >= 0.9:
    print("Letter Grade = A")
elif s >= 0.8:
    print("Letter Grade = B")
elif s >= 0.7:
    print("Letter Grade = C")
elif s >= 0.6:
    print("Letter Grade = D")
else:
    print("Letter Grade = F")
```

## Total Pay 
[ex_ifstatements.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/ex_ifstatements)

``` python
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
pay = 0

if h <= 40:
    #print regular pay
    pay = h * r
else:
    #print overtime pay
    pay = 40 * r 
    h = h - 40
    r = r * 1.5
    pay = pay + h * r

print(pay)
```

## Lists and File Input 
[ex_lists.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/ex_lists)

``` python
fname = input("Enter file name: ") #romeo.txt
fh = open(fname) #opens file
lst = list()
for line in fh: #itterates throgh every word in file
    print(line.rstrip())
    lst.append(line) #appends words to list
    print(list())
```

## Try and Except 
[ex_try_except.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/ex_try_except)

``` python
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try: #tries h and r as float values
    h = float(hrs)
    r = float(rate)
except: #prints error if h or r are not float values
    print("Error, please enter numeric input")
    quit()

pay = 0

if h <= 40:
    #print regular pay
    pay = h * r
else:
    #print overtime pay
    pay = 40 * r 
    h = h - 40
    r = r * 1.5
    pay = pay + h * r

print(pay)
```

## User Inputs 
[ex_user_input.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/ex_user_input)

``` python
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
pay = float(hrs) * float(rate)
print("Pay:", pay)
```

## Find and Extract 
[find_extract.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/find_extract)

``` python
text = "X-DSPAM-Confidence:    0.8475"
x = text.find('0')
y = text[x:]
print(float(y))
```

## HTML Scraping 
[html_scraping_01.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/html_scraping_01/bs4)

``` python
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

count = 0
lst = list()
new_lst = list()
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    count = count + 1 #counts the number of lines
    words = tag.decode().split('>') #splits infront of numbers we need out
    for word in words:
        x = word.split('<') #splits after the numbers we need, leaving just the numbers and a ton of random strings
        lst.append(x) #add everything to lst
        for line in x: #searches through our list
            line = line.rstrip() #strips whitespace from the right
            xx = re.findall('[0-9]+', line) #finds all the numbers
            for value in xx:
                new_lst.append(value) #adds all str('numbers') values into new list
            for i in range(0, len(new_lst)): #searches through lst and turns each str to int
                new_lst[i] = int(new_lst[i])
                
print("Count", count)
print("Sum", sum(new_lst))
```

## Sockets 
[http_ex_01.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/http_ex_01)

``` python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
```

## Check Internet Connection 
[Internet_Check.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/Internet_Check)

``` python
import requests
from requests.exceptions import ConnectionError

def internet_connection_test():
	url = 'https://www.google.com/'
	print(f'Attempting to connect to {url} to determine internet connection status.')
	
	try:
		print(url)
		resp = requests.get(url, timeout = 10)
		resp.text
		resp.status_code
		print(f'Connection to {url} was successful.')
		return True
	except ConnectionError as e:
		requests.ConnectionError
		print(f'Failed to connect to {url}.')
		return False
	except:
		print(f'Failed with unparsed reason.')
		return False

internet_connection_test()
```

## URL Links 
[link_search_01.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/link_search_01/bs4)

``` python
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('URL:', tag.get('href', None))
    print('Contents:', tag.contents[0])
    print('Attrs:', tag.attrs)
```

## Random Password Generator 
[password.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/rand_password)

``` python
import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

# pass_len=random.randint(8,13)  #without User INput
pass_len = int(input("Enter Password Length"))

# length of password by 50-30-20 formula
alpha_len = pass_len//2
num_len = math.ceil(pass_len*30/100)
special_len = pass_len-(alpha_len+num_len)


password = []


def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)


# alpha password
generate_pass(alpha_len, alpha, True)
# numeric password
generate_pass(num_len, num)
# special Character password
generate_pass(special_len, special)
# suffle the generated password list
random.shuffle(password)
# convert List To string
gen_password = ""
for i in password:
    gen_password = gen_password + str(i)
print(gen_password)
```

## Read File \#1 
[read_file.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/read_file)

``` python
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
fread = fh.read()
print(fread.upper().rstrip())
```

## Read File \#2 
[read_file_02.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/read_file_02)

``` python
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
```

## Read File \#3 
[read_file_03.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/read_file_03)

``` python
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
```

## Read File \#4 
[read_file_04.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/read_file_04)

``` python
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
```

## Regular Expressions 
[reg_exp_01.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/reg_exp_01)

``` python
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
```

## Regular Expressions Shortened 
[shortened.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/reg_exp_01)

``` python
import re
print( sum( [ int(i) for i in re.findall('[0-9]+',open("actual.txt").read()) ] ) )
```

## Tuples 
[tuples_01.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/tuples_01)

``` python
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
```

## XML Data Extraction 
[XML_Data_Extract.py](https://github.com/rgerjeki/Python-for-Everybody/tree/main/XML_Data_Extract)

``` python
from urllib.request import urlopen
import urllib
import xml.etree.ElementTree as ET

url = input("Enter location: ")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_200531.xml"
print("Retrieving " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

x = 0

for count in counts:
    x += int(count.text)

print("Sum:" + str(x))
```