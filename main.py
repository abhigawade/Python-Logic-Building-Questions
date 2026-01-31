# Python Practice Questions for Logic Building

# Sort List without using sort function
li = [2,6,1,5,8]
for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
print(li)
