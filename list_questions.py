
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
