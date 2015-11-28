import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false',
                                        'address': address})
    print 'Retrieving', url
    js = json.loads(str(urllib.urlopen(url).read()))
    print 'Retrieved',len(str(urllib.urlopen(url).read())),'characters'
    if 'status' not in js or js['status'] != 'OK' :
        print '=== Failure To Retrieve'
        continue

    location = js['results'][0]['place_id']
    print 'Place id',location
