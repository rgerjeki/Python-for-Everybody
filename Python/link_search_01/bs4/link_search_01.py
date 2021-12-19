import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

curr_c = 0
def parse_html(url): #creates a function def where we can call back to it
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')
    return tags
url = input('Enter - ')
c = input("Enter count:")
p = input("Enter position:")

int_c = int(c) #convert to int
int_p = int(p) #convert to int
while curr_c < int_c:
    print('Retrieving: ', url)
    tags = parse_html(url) #sets tags equal to our function def
    for index, item in enumerate(tags): #enumerate is a counter, counts through the tags
        if index == int_p - 1:
            url = item.get('href', None) #sets url to our new url
            break
        else:
            continue
    curr_c += 1 #counts up until it reaches value int_c
print('Last Url: ', url)
"""
#Wrong way, still clever way of getting certain words into a list
    links = tag.decode().split('"')
    for name in links:
        x = name.split('<')
        lst.append(x)
        for line in x: #searches through our list
            line = line.rstrip() #strips whitespace from the right
            xx = re.findall('>(\S*[a-zA-Z])', line) #finds all the numbers
            for value in xx:
                new_list.append(value) #adds all str('numbers') values into new list
"""