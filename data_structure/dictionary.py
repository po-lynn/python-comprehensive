
person = {'name': 'John', 'age': 20, 'weight': 60, 'office': 'GCA'}
# Check if the name and tel keys are in the person dictionary
print('name' in person, 'tel' in person)    # True False
# Modify the corresponding value in the person dictionary to 25 through age repair
if 'age' in person:
    person['age'] = 25
# Store new key-value pairs into the person dictionary through index operations
person['tel'] = '13122334455'
person['signature'] = 'My Signature'
# Check the number of key-value pairs in the person dictionary
print('name' in person, 'tel' in person)    # True True

print(len(person))    # 6
# Loop through the keys of the dictionary and get the value corresponding to the key through the index operation
for key in person:
    print(f'{key}: {person[key]}')





# The value in the dictionary is another dictionary (nested dictionary)
students = {
    1001: {'name': 'John', 'sex': True, 'age': 22, 'place': 'Hlaing'},
    1002: {'name': 'Doe', 'sex': True, 'age': 23, 'place': 'SouthOkkalar'},
    1003: {'name': 'Steve', 'sex': False, 'age': 20, 'place': 'NorthOkkalar'}
}

# Use the get method to get the corresponding value through the key. 
# If it cannot be obtained, it will not cause a KeyError exception but return None or the default value set
print(students.get(1002))    #
print(students.get(1005))    # None


# Get all the keys in the dictionary
print(students.keys())      # dict_keys([1001, 1002, 1003])
# Get all the values in the dictionary
print(students.values())    # dict_values([{...}, {...}, {...}])

# Get all the key-value pairs in the dictionary
print(students.items())     # dict_items([(1001, {...}), (1002, {....}), (1003, {...})])

# Loop through all key-value pairs in the dictionary
for key, value in students.items():
    print(key, '--->', value)

# Use the pop method to delete the corresponding key-value pair through the key and return the value
stu1 = students.pop(1002)
print(stu1)             # 
print(len(students))    # 2
# stu2 = students.pop(1005)    # KeyError: 1005
stu2 = students.pop(1005, {})
print(stu2)             # {}

# Use the popitem method to delete the last set of key-value pairs in the dictionary and return the corresponding two-tuple
# If there is no element in the dictionary, calling this method will raise a KeyError exception
key, value = students.popitem()
print(key, value)    # 1003 

# If the key exists in the dictionary, setdefault returns the original value corresponding to the key
# If the key does not exist in the dictionary, add a key-value pair
#  to the dictionary and return the value of the second parameter, which defaults to None
result = students.setdefault(1005, {'name': 'John', 'sex': True})

print(result)        # 
print(students)      # {1001: {...}, 1005: {...}}

# Use update to update the dictionary elements, 
# the same key will overwrite the old value with the new value, and the different key will be added to the dictionary
others = {
    1005: {'name': 'Maung Maung', 'sex': True, 'age': 32, 'place': 'Insein'},
    1010: {'name': 'Aye Aye', 'sex': False, 'age': 19},
    1008: {'name': 'Sein Sein', 'sex': False}
}
students.update(others)
print(students)      # {1001: {...}, 1005: {...}, 1010: {...}, 1008: {...}}


"""
We explain the application of dictionaries through a few simple examples.

Example 1 : Enter a paragraph and count the number of occurrences of each English letter.
"""
sentence = input('Please enter a paragraph:')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
for key, value in counter.items():
     print(f'letter {key} appeared {value} times.')




"""Example 2 : Save the stock code and price in a dictionary, find out the stocks whose stock price is greater than 100 yuan and create a new dictionary.

Explanation : This new dictionary can be created using the dictionary's generative syntax.
"""
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stocks2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks2)
