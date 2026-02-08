
# List Questions
# Interchange first and last elements in a list

li_one = [1,4,7,3,9,4,2]

li_one[0], li_one[-1] = li_one[-1], li_one[0]

print(li_one)

# Find Largest element in List
li_one = [1,4,3,7,5,8,2]
max_ele = li_one[0]
for i in li_one:
    if i > max_ele:
        max_ele = i
        
print(max_ele)

# Find smallest element in List
li_one = [1,4,3,7,5,8,2]
min_ele = li_one[0]
for i in li_one:
    if i < min_ele:
        min_ele = i
        
print(min_ele)

#Sum of Number Digits in List in Python
li_one = [123, 456, 789]
li_two = []
for i in li_one:
    tot = 0
    while i > 0:
        dig = i % 10
        tot = tot + dig
        i = i // 10
    li_two.append(tot)
print(li_two)

#Remove Duplicates from a List in Python
li_one = [1,3,2,4,5,6,3,1,7,5,9]
li_two = []
for i in li_one:
    if i not in li_two:
        li_two.append(i)
        
print(li_two)

# Find second largest element in list
li_one = [1, 2, 4, 8, 5, 4]

max_ele = float('-inf')
sec_max = float('-inf')

for i in li_one:
    if i > max_ele:
        sec_max = max_ele
        max_ele = i
    elif i > sec_max and i != max_ele:
        sec_max = i

print(sec_max)

# Reverse a List k times
li_one = [1,2,3,4,5]   #[4,5,1,2,3]
k =  2
for i in range(1, k+1):
    val = li_one.pop()
    li_one.insert(0,val)
    
print(li_one)

#Merge Two Lists
li_one = [1,2,3]
li_two = [4,5,6]

for i in li_two:
    li_one.append(i)
    
print(li_one)

# Method two
li_one.extend(li_two)
print(li_one)

# Move all zeros to end
li_one = [1,4,7,0,3,0,2,5,0,6]
n = len(li_one)
for i in range(0,n):
    if li_one[i] == 0:
        val = li_one.pop(i)
        li_one.append(val)
        
print(li_one)
