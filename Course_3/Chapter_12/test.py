
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


link = 'http://py4e-data.dr-chuck.net/comments_237500.xml'
html = urlopen(link)
soup = BeautifulSoup(html, "lxml")

sums = 0
nums = soup.find_all('count')
for num in nums:
    sums += int(num.text)

print(sums)

