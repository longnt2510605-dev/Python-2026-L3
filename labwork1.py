#ex1 
def AreaOfCircle():
    r = int(input('input radius:'))
    if r >= 0:
        print("area is:" + str(r**2*3.14))
    else:
        print('invalid')

AreaOfCircle()

#ex2
def Convert():
    c = float(input('input celcius:'))
    f = c * 1.8 + 32
    print(f'is {f} F ')
Convert()

#ex3
def Prime():
    p = int(input('input a number:'))
    check = 0
    for i in range (1,p):
        check += i
    if p == check:
        print('that is a prime number')
    else:
        print('that is not a prime number')
Prime()

#ex4
def Perfect():
    p = int(input("input a number:"))
    check = 0
    for i in range(1,p):
        if p % i == 0:
            check += i
    if p == check:
        print('that is a perfect number')
    else:
        print('that is not a perfect number')

#ex5
def Color():
    list_color = ['red','blue','yellow','white']
    c = str(input('input your color:'))
    for i in range(0, len(list_color)):
        if list_color[i] == c:
            print(f'your color is at index {i+1} in my list')

Color()

#ex6
def range1():
    range1 = []
    for i in range(0, 7):
        range1.append(i)
    print(range1)
range1()

def range2():
    range2 = []
    for i in range(1, 10, 3):
        range2.append(i)
    print(range2)
range2()

def range3():
    range3 = []
    for i in range(1, 6):
        range3.insert(0,i)
    print(range3)
range3()

def range4():
    range4 = []
    for i in range(-2, 7, 2):
        range4.insert(0,i)
    print(range4)
range4()

#ex7
def remove_dollar_sign():
    s = str(input('enter your string:'))
    if '$' in s:
        s = s.replace('$', '')
    print(f'new string: {s}')
remove_dollar_sign()

#ex8
def extract_even():
    I = [1,4,5,-1,10]
    check = []
    for i in range(0,len(I)):
        if I[i] % 2 == 0:
            s = I[i] 
            check.append(s)
    print(check)
extract_even()

#ex9
a = int(input('input a number:'))
def factorial(a):
    f = 1
    if a <= 0:
        print('invalid')
    else:
        for i in range(1, a+1):
            f *= i
        print(f'factorial of {a} is {f}')
factorial()

#ex10
def divisors():
    d = int(input('input a number:'))
    list = []
    for i in range(1,d):
        if d % i == 0:
            list.append(i)
    print(list)
divisors()

#ex11
import math
def distance():
    x1 = float(input('coordinates of point1(x1)'))
    y1 = float(input('coordinates of point1(y1)'))
    x2 = float(input('coordinates of point2(x2)'))
    y2 = float(input('coordinates of point2(y2)'))
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print(f'the distance is: {d}')
distance()

#ex12
def function():
    for i in range(0,4):
        if i == 0 or i == 3:
            print('*' * 5)
        else:
            print("*" + " "*3 + "*")
function()
    


