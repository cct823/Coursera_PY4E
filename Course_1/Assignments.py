# Python for Everybody Specialization
# Course 1 - Programming for Everybody (Getting Started with Python)
# Name: Tim Chen
# Date: 10/25/2019

# Assignment 1
print("hello world")


# Assignment 2.2
name = input("Enter your name")
print("Hello " + name)


# Assignment 2.3
hrs = input("Enter Hours:")
rate = input("Enter Rates:")
print('Pay:', float(hrs)*float(rate))


# Assignment 3.1
hrs = input("Enter Hours:")
rate = input('Enter Rate:')
h = float(hrs)
r = float(rate)
if hrs > 40:
    print((h-40)*(r*1.5)+40*r)


# Assignment 3.3
score = input("Enter Score: ")
score = float(score)

if score >=0.9:
    print('A')
elif 0.9>score>=0.8:
    print('B')


# Assignment 4.6
def computepay(h, r):
    if h > 40:
        s = (h - 40) * (r * 1.5) + 40 * r
    return s

hrs = float(input("Enter Hours:"))
rate = float(input('Enter rate'))
p = computepay(hrs, rate)
print(p)

# Assignment 5.2
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            int(num)
        except:
            print('Invalid input')
            continue
        num = int(num)
        if smallest is None:
            smallest = largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print("Maximum is", largest)
print("Minimum is", smallest)


# Course 1 Completed.









