# Python for Everybody Specialization
# Course 2 - Data Structure
# Name: Tim Chen
# Date: 10/25/2019


# Assignment 6.5

text = "X-DSPAM-Confidence:    0.8475"
p = text.find('0')
print(float(text[p:]))


# Assignment 7.1
'''file name words.txt'''
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    text = line.rstrip().upper()
    print(text)

# Assignment 7.2
'''file name: mbox-short.txt'''
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    text = line.rstrip().upper()
    print(text)
# Assignment
fname = input("Enter file name: ")
fh = open(fname)
value = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        p = line.find('0')
        a = float(line[p:])
        value += a
        count += 1
print('Average spam confidence:', value / count)


# Assignment 8.4
'''file name: remeo.txt'''
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split('\n')[0]
    word = words.split(' ')
    for item in word:
        if item in lst:
            continue
        else:
            lst.append(item)
lst.sort()
print(lst)


# Assignment 8.5
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0

for lines in fh:
    a = lines.startswith('From ')
    if a == True:
        line = lines.split(' ')[1]
        print(line)
        count += 1
print("There were", count, "lines in the file with From as the first word")

# Assignment 9.4
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
count = 0
elist = []

for lines in handle:
    a = lines.startswith('From ')
    if a == True:
        line = lines.split(' ')[1]
        elist.append(line)

cleand = {}
for email in elist:
    if email not in cleand:
        cleand[email] = 1
    else:
        cleand[email] += 1

value = 0
for emails in cleand:
    if cleand[emails] >= value:
        name = emails
        value = cleand[emails]
print(name, value)


# Assignment 10.2
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hours = []

for lines in handle:
    a = lines.startswith('From ')
    if a == True:
        hour = lines.split(':')[0][-2:]
        hours.append(hour)

hours = sorted(hours)

hoursd = {}

for hour in hours:
    if hour not in hoursd:
        hoursd[hour] = 1
    else:
        hoursd[hour] += 1

for item in hoursd.keys():
    print(item, hoursd[item])

# Course 2 Completed.









