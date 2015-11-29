import re
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
if len(url) < 1:
    url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_202735.html'
if url == 'a':
    url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_42.html'

print sum([int(v) for v in re.findall('.*<span.+>(\d+)\D+?', str(BeautifulSoup(urllib.urlopen(url).read(), "html.parser")))])
