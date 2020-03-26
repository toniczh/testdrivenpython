from lxml import etree
from bs4 import BeautifulSoup
import urllib
cin_file = "C:\\temp\\cin\\36352102.xml"
source_file = urllib.urlopen("file://"+cin_file).read()
bs = BeautifulSoup(source_file,"xml")
receiver = bs.find('sh:Receiver')
print(receiver)