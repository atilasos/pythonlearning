import re
import urllib
import ssl
from bs4 import BeautifulSoup as BS
# get url and other user data
url = raw_input('Enter url: ')
counter = raw_input('Enter count: ')
pos = raw_input('Enter pos: ')
counter = int(counter)
pos = int(pos)
pos = pos - 1
# shortcut for ass data
if len(url) < 1:
    url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Dania.html'
if url == 'a':
    url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html'
# looping to get data
count = 0
lst = list()
while count < counter:
    print 'Retrieving:', url
    for v in re.findall('.*<a.+(http.+?ml).*?', str(BS(urllib.urlopen(url, context=ssl.SSLContext(ssl.PROTOCOL_TLSv1)).read(), "html.parser"))):
        lst.append(v)
    url = lst[pos]
    lst = list()
    count += 1
print 'Last Url:', url
#
# loo
#
