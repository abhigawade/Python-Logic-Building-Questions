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
