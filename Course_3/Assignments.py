# Python for Everybody Specialization
# Course 3 - Using Python to Access Web Data
# Name: Tim Chen
# Date: 10/25/2019


# Assignment 1
# Extracting Data With Regular Expressions
import re
x = open('regex_sum_237496.txt')
NumList = []
for line in x:
    y = re.findall('[0-9]+',line)
    if len(y) != 0:
        for i in range(len(y)):
            NumList.append(int(y[i]))

print(NumList)
print(sum(NumList))
# Ans: 426754


# Assignment 2
# Understanding the Request / Response Cycle
import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data)) < 1 :
        break
    print(data.decode())
mysock.close()
''' Answers: 
HTTP/1.1 200 OK
Date: Fri, 25 Oct 2019 22:37:05 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain
'''


# Assignment 3
# Scraping HTML Data with BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_237498.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
sum = 0
for tag in tags:
    sum += int(tag.contents[0])
print(sum)
# Ans: 2432


# Assignment 4
# Following Links in HTML Using BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
# url = http://py4e-data.dr-chuck.net/known_by_Edie.html
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# get user input for how many times to search
count = int(input('Enter count:'))
# count = 7
# get user input for which url to click on
position = int(input('Enter position:'))-1
# position = 18
while count >= 0:
    # re-reads the current url
    html = urllib.request.urlopen(url, context=ctx).read()
    # creates a new soup object
    soup = BeautifulSoup(html, 'html.parser')
    # searches the page for all <a> tags
    tags = soup('a')
    print("Retrieving: ", url)
    # upates the current url
    url = tags[position].get("href", None)
    count = count - 1
# Answer: Rianna


# Assignment 5
# Extracting Data from XML
from urllib.request import urlopen
from bs4 import BeautifulSoup

link = 'http://py4e-data.dr-chuck.net/comments_237500.xml'
html = urlopen(link)
soup = BeautifulSoup(html, "lxml")
sums = 0
nums = soup.find_all('count')
for num in nums:
    sums += int(num.text)
print(sums)
# Ans: 2168


# Assignment 6
# Extracting Data from JSON
import urllib.request, json
url = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_237501.json')
data = json.loads(url.read().decode())
sum = 0
for i in range(len(data['comments'])):
    score = data['comments'][i]['count']
    sum += score
print(sum)
# Ans: 2120


# Assignment 7
# Assignment Using the GeoJSON API
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    print(js['results'][0]['place_id'])

# Ans: ChIJSXQyV43NvYcRdRt537z5Zg0

# Course 3 Completed.
