# String Questions
# Check String is Palindrome or not
str_one = 'nitin'
rev_str = str_one[::-1]
if str_one == rev_str:
    print('String is Palindrome')
else:
    print('String is not Palindrome')


# Find a Length of string
# First Method
st = 'hello_world'
print(len(st))

# Second Method
count = 0
for i in st:
    count += 1
print(count)

#Remove Letters From a String in Python
st_one = 'hello world'
st_two = ''
for i in st_one:
    if i != 'l':
        st_two += i
    
print(st_two)

# Avoid Spaces in string length
# Method one
st_one = 'hello world '
count = 0
for i in st_one:
    if i != ' ':
        count += 1
        
print(count)
# Method two
s = "geeks for geeks"
res = len(s.replace(" ", ""))
print(res)

# Print even length words in a string
st_one = "This is a python language"
st_list = st_one.split()

c = [ i for i in st_list if len(i)% 2 == 0]
print(c)
new_st = ' '.join(c)
print(new_st)

# Uppercase Half String
# Method 1
st_one = 'helloworlduser'
length = len(st_one)
st_two = ''
for i in range(0, length//2):
    upper_word = st_one[i].upper()
    st_two += upper_word

print(st_two)

# Method 1
st_one = 'helloworlduser'
length = len(st_one)//2
st_two = st_one[:length].upper() + st_one[length:]
print(st_two)

# Make first letter of every word of string capital
st_one = 'my name is a abhi'
li_one = st_one.split()
print(li_one)

li_two = []
for i in li_one:
    if len(i) == 1:
        new_i = i.upper()
    else:
        new_i = i[0].upper() + i[1:-1] + i[-1].upper()
    li_two.append(new_i)
    
new_str = ' '.join(li_two)
print(new_str)

#check if a string has at least one letter and one number
st_one = 'my name is a abhi age 23 '

for i in st_one:
    flag = True if i.isalpha() or i.isdigit() else False
    if flag:
        break

if flag:
    print('Yes it has')
else:
    print('No')

# Get desired output from string
str_one = 'a3b2c1'
output_str = 'aaabbc'
str_two = ''
n = len(str_one)
for i in range(0, n, 2):
    str_two += str_one[i] * int(str_one[i+1])
print(str_two)
