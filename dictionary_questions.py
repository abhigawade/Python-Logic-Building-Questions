# Sort a dictionay using sorted method
d = {'watermelon': 3, 'apple': 4, 'banana': 1, 'mango': 2}

new_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(new_dict)
# sorted method used to sort list, dict by items, keys, dict.items()

