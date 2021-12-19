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