import json
data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
#info = json.loads(data)
print 'Name:', json.loads(data)["name"]
print 'Hide:', json.loads(data)["email"]["hide"]
