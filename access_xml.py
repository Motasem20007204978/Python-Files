import xml.etree.ElementTree as ET
from urllib import request

xml = request.urlopen('http://py4e-data.dr-chuck.net/comments_1452491.xml')
#print(type(xml.read().decode()))#str
data = xml.read().decode()#file content as text
# decode method to convert bytes to string
print(len(data))
tree = ET.fromstring(data)#parse text into xml
all_counts = tree.findall('.//count')#extract elements
print(len(all_counts))
print(sum([int(element.text) for element in all_counts]))
