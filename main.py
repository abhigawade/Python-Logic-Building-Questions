# Python Practice Questions for Logic Building

# write a program to check num is even or odd

def even_odd(num):
    if(num%2 == 0):
        print('Number is even')
    else:
        print('Number is odd')
        
even_odd(2)

# Write a program to check year is leap year or not

year = int(input('Enter a year : '))
if(year % 2 == 0):
    print('Year is leap year')
else:
    print('Year is not a leap year')

# Script to add two numbers
def add(num1, num2):
    return num1 + num2

addition = add(2,4)
print(addition)

# Write a program to remove duplicate from list of string

list_one = ['jay', 'sai', 'jay', 'nayan', 'sanket', 'sai' ]

for i in list_one:
    if list_one.count(i) > 1:
        list_one.remove(i)
        
print(list_one)
    
    
# print first natural numbers

for i in range(1,11):
    print(i)

# print first natural numbers in reverse order
for i in range(10,0,-1):
    print(i)

# script to reverse a tuple

tuple_one = (2,4,6,7,9)
rev_tuple = tuple(tuple_one[::-1])
print(rev_tuple)

# Python script to print index of all occurrence of given element in a given list

list_one = [3,6,7,8,1,2]
list_two = []

for i in list_one:
    ind = list_one.index(i)
    list_two.append(ind)
    
print(list_two)
    
    
# Python function to return next prime number
        
def get_prime(n):
    while(True):
        n += 1
        for i in range(2, n):
            if n % i ==0:
                break
        else:
            return n
                
print(get_prime(11))
        

# Python script to create a list of first N prime numbers


# Area of circle

def area_circle(r):
    pi = 3.14
    area = pi * r * r
    print(area)
    
area_circle(3)


# single line function to find factorial of a number

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))

# # Remove duplicate from string
ab = 'muaoebma'
cd = ''
for i in ab:
    if i not in cd:
        cd += i
        
print(cd)

# Program to remove white spaces in string without using inbuilt function
str = 'abh srsf wq s'
str1 = ''
for i in str:
    if i != ' ':
        str1+=i
print(str1)

# Python script to reverse a string
str1 = 'abhishek'
rev_str = str1[::-1]
print(rev_str)

# Print table of 5
for i in range(1,11):
    n=5*i
    print(f'5 * {i} = {n}')

#  Table of users choice
num = int(input('Enter a munber :'))
for i in range(1,11):
    mul = num*i
    print(f'{num} * {i} = {mul}')
    
# Python script to print first n odd natural numbers
num = int(input('Enter a munber :'))
print('1')
for i in range(1, num+1):
    print(2*i+1)

# Python script to print first n even natural numbers
num = int(input('Enter a munber :'))
for i in range(1, num+1):
    print(2*i)


# # Python script to print first n natural numbers

n = int(input('Enter a munber :'))
for i in range(1,n+1):
    print(i)

#sort list of numbers
li = [1,5,2,3,8]
li.sort()
print(li)

#list to string conversion 
li = ['python', 'is', 'good']
a = ""
for i in li:
    a += i
    a += ' '
print(a)

#palindrome of string
st1 = 'naman'
st2 = st1[ : : -1]
if st1 == st2:
    print('string is palindrome')
else:
    print('string is not palindrome')
    
#Remove duplicate character of string

st = ''
st2 = 'ppythoon'
for i in st2:
    if i not in st:
        st +=i
print(st)

#count element in list withoiut using len()
li = [11,12,13,14,15]
count = 0
for i in li:
    if i:
        count += 1
print(count)

#Reverse a list
li = [1,2,3,4,5]
li.reverse()
print(li)

# Without function 
li = [1,2,3,4,5,6]
n = len(li)
li2 = []
for i in range(n-1, -1, -1):
    if i:
        li2.append(li[i])
        
print(li2)

# max element in list without using max()
li = [1,3,6,4,8]
max = 0
for i in li:
    if i > max:
        max =i
        
print(max)

#Count Total cost
class fruit:
    def __init__(self, quantity, cost):
        self.quantity = quantity
        self.cost = cost
    
    def total_cost(self):
        total_price  = self.quantity * self.cost
        print(total_price)
        
mango = fruit(2,50)
mango.total_cost()

# li = [1,2,3,4,5,6,7,8]
a = li[0:5] #12345
b = li[-1:-5:-1]#8765
c = li[ : 3]#123
d = li[ 3:]#45678
e= li[-2:]#78
f= li[ :-1]#1234567

# print(a,b,c,d,e,f)

#concat tuple
a = (1,2,3)
b = (4,5,6)
c= a+b
print(c)

# concat list
li = [1,2,3,4]
li2 = [5,6,7]
li3 = li + li2
print(li3)

# li.extend(li2)
# print(li)

# for i in li2:
#     li.append(i)
    
# print(li)

# class employee:
#     name = "abhishek"
#     id = 12
    
# ob = employee()
# print(ob.id)
# print(ob.name)

#Flatten a nested list
li = [[1,2],[3,4],[5]]
li2 = []

for i in li:
    li2.extend(i)
    
print(li2)

#check a list is palindrome or not
li = [1,2,3,2,1]
li2 = li[::-1]
print(li2)
if li == li2:
    print('List is palindrome')
else:
    print('Not Palindrome')

#count a frequency of each element in list with with dictionary
li = [1,3,5,2,1,5,3,1,7]
dict = {}
for i in li:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
        
print(dict)

#Merge two dictionaries
dict = {1:'a', 2:'b'}
dict2 = {3:'a', 4:'b'}

for key,value in dict2.items():
    if key not in dict:
        dict[key] = value
        
print(dict)

#sort a list without using sort function

li = [2,1,5,7,9,4]
n = len(li)

for i in range(0, n):
    for j in range(i+1, n):
        if li[i] >=li[j]:
            li[i] , li[j] = li[j] , li[i]
            
print(li)

#rotate a list by k elements

li = [1,2,3,4,5,6]
k = 2

for _ in range(k):
    li.insert(0, li.pop())
    
print(li)

#fibonacci series
a = 0
b = 1
n = 10
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c)

# Biggest char in list
li = ['hi', 'hello', 'new', 'chat']
bl = 0
word = ''
for i in li:
    l = len(i)
    if l > bl:
        bl = l
        word = i
print(word)

#factorial of number
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

result = fact(5)
print(f'Factorial is {result}')


#Fibonacci series using a generator
# def genarator_fun():
#     a,b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b
        
# f1 = genarator_fun()
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))

# Sort a dictinory 
dict1 = { 11:'Abhi', 18:'Rohan', 14:'Rohit', 13:"Ajay"}

s = sorted(dict1.keys())
dict2 = {}
for i in s:
    dict2[i] = dict1[i]
    
print(dict2)

# Find a pair with given number in a list

li = [1,5,3,7,9,4,6]
k = 7
n = len(li)
for i in range(n):
    for j in range(i+1,n):
        if i+ j == k:
            print(i,j)

#Linear Search
li = [1,2,3,4,5,6,7,8,9]
target = 3
for i in range(len(li)):
    if li[i] == target:
        print(f'Element found at index {i}')
        break
else:
    print('Element not found')



# Sort List without using sort function
li = [2,6,1,5,8]
for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
print(li)

# Add list items into dictionary as key and its count as value
li = [1,3,5,2,1,5,6,3,3]
new_dict = {}
for i in li:
    new_dict[i] = li.count(i)
    
print(new_dict)

# Second Way
li_one = [1,4,3,5,7,3,1,5,3,5,7,2]
dict_one = {}

for i in range(0, len(li_one)):
    if li_one[i] in dict_one:
        dict_one[li_one[i]] += 1
    else:
        dict_one[li_one[i]] = 1
        
print(dict_one)

# Third Way 
li_one = [1,4,3,5,7,3,1,5,3,5,7,2]
dict_one = {}
for i in range(0, len(li_one)):
    dict_one[li_one[i]] = dict_one.get(li_one[i], 0) + 1
    
print(dict_one)
# Time Complexity O(n)
# Space Complexity O(n)
