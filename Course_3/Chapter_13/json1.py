import urllib.request, json

url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_237501.json')
data = json.loads(url.read().decode())

# with urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_237501.json') as url:
#     data = json.loads(url.read().decode())
#     print(data)

sum = 0

for i in range(len(data['comments'])):
    score = data['comments'][i]['count']
    sum += score

print(sum)
#2120
