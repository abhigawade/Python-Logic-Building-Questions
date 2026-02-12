# Sort a dictionay using sorted method
d = {'watermelon': 3, 'apple': 4, 'banana': 1, 'mango': 2}

new_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(new_dict)
# sorted method used to sort list, dict by items, keys, dict.items()

# Get a length of dictionary
dict_one = {1 : 'a', 2: 'b', 3: 'c', 4: 'd'}
len = 0
for i in dict_one.keys():
    if i:
        len += 1
        
print(f'Lenght of dictionary is {len}')


# Merge two dictionary 
# Method 1
dict_one = {'x': 1, 'y': 2}
dict_two = {'y': 3, 'z': 4}

dict_three = dict_one | dict_two
print(dict_three)

# Method 2
for i in dict_two.keys():
    print(i)
    if i not in dict_one.keys():
        dict_one[i] = dict_two[i]
        
print(dict_one
