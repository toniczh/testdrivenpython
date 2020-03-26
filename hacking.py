from lxml import etree
from bs4 import BeautifulSoup
import urllib.request
cin_file = "C:\\temp\\cin\\36352102.xml"
url_file = urllib.request.pathname2url(cin_file)
# print(url_file)
source_file = urllib.request.urlopen("file:"+url_file).read()
bs = BeautifulSoup(source_file,"xml")
# find the receiver
receiver = bs.find('sh:Receiver')
receiver_id= receiver.find("sh:Identifier").get_text()
print(receiver_id) 