import json
import urllib
#a for actual file and s for debug
while True:
    url = raw_input('Enter "a" for actual data and "s" for sample data: ')
    if url == 'a':
        url='http://python-data.dr-chuck.net/comments_202736.json'
        data='actual :'
    elif url == 's':
        url='http://python-data.dr-chuck.net/comments_42.json'
        data='sample :'
    else: exit()
    print '*Working with ' + data, url
    #getting the data
    js = json.loads(str(urllib.urlopen(url,).read()))
    #sum and print
    print sum([ line["count"] for line in js["comments"] ])
