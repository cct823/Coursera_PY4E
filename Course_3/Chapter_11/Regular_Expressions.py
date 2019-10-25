import re

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)

'''x = open('regex_sum_237496.txt')
NumList = []
for line in x:
    y = re.findall('[0-9]+',line)
    if len(y) != 0:
        for i in range(len(y)):
            NumList.append(int(y[i]))

print(NumList)
print(sum(NumList))'''
