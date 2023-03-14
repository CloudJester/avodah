import requests

url = 'http://127.0.0.1:8000/jobs/'
myobj = {
    'name': 'zach',
    'image': 'redis/redis:v2',
    }

x = requests.post(url, json = myobj)
print(x.text)

url = 'http://127.0.0.1:8000/jobs/1'

x = requests.delete(url)
print(x)
