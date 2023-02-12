import requests
import json

def delete(id):
    requests.delete(f'http://10.1.170.242:8080/api/tests/{id}')

def post(data):
    requests.post('http://10.1.170.242:8080/api/tests',
                data = data)



# requests.delete('http://10.1.170.242:8080/api/tests/63e7e599d815327e8e987cd5')
# requests.post('http://10.1.170.242:8080/api/tests',
#     data = {
#         'text': 'Hello, Goodbye.'
#     })


# requests.put('http://10.1.170.242:8080/api/tests/63e7eb9efbc9dcd98f022dab', 
# data = {
#     'text': 'S(he) be(lie)ve(d)'
# })

requests.delete('http://10.1.170.242:8080/api/tests/63e7eb9efbc9dcd98f022dab')

x = requests.get('http://10.1.170.242:8080/api/tests')


xs = json.loads(x.text)

for thing in xs:
    print(thing)