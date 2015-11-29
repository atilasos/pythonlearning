import urllib
import xml.etree.ElementTree as ET
# get url
url = raw_input('Enter url - ')
# shortcut for ass data
if len(url) < 1:
    url = 'http://python-data.dr-chuck.net/comments_202732.xml'
if url == 'a':
    url = 'http://python-data.dr-chuck.net/comments_42.xml'
print sum([int(v.text) for v in ET.fromstring(urllib.urlopen(url).read()).findall('.//count')])
