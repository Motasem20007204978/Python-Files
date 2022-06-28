import json
from urllib.request import urlopen
from urllib.parse import urlencode

connection = urlopen('http://py4e-data.dr-chuck.net/comments_1452492.json')
data_file = connection.read().decode()

print(len(data_file))

data = json.loads(data_file)
comments = data['comments']
counts = [x['count'] for x in comments]
print(len(counts))
print(sum([int(v) for v in counts]))


#////////////////////////////////////////

url = 'http://py4e-data.dr-chuck.net/json?'
address = urlencode({'address':'Florida Atlantic University','key':42})
url = url.__add__(address)
print(url)

connection = urlopen(url)
data_file = connection.read().decode()
data = json.loads(data_file)
print(len(data_file))
print(data['results'][0]['place_id'])

data = '''{
    "name":"Motasem",
    "phone":{
        "type":"int1",
        "number":"+972597204978"
    },
    "email":{
        "hide":"yes",
        "address":"motasemalmobayyed@gmail.com"
    },
    "courses":{
        "python":{
            "day":{
                "sunday":"5-9"
            }
        }
    }
}
'''

information = json.loads(data)#dectionary of 3 items (name, phone dectionary, and email dectionary)

print(information['name'])
print(information['phone']['number'])