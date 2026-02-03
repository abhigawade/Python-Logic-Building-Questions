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
