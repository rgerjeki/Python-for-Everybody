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