import requests

link = "http://192.168.1.20:8000/users/?format=json"
f = requests.get(link)
print(f.text)
p= open("log.txt","w+")
p.write(f.text)