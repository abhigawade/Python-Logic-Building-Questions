# Python Practice Questions for Logic Building

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
