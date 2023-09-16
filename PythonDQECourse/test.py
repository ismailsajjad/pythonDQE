# #this file is created for testing purpose

dict1 = {'a': 5, 'b': 3, 'c': 7}
dict2 = {'b': 8, 'c': 4, 'd': 6}

# Create a merged dictionary
merged_dict = {}

# Merge dict1 into merged_dict
for key, value in dict1.items():
    if key in merged_dict:
        merged_dict[key] = max(merged_dict[key], value)
    else:
        merged_dict[key] = value

# Merge dict2 into merged_dict
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] = max(merged_dict[key], value)
    else:
        merged_dict[key] = value

# Print the merged dictionary
print(merged_dict)

