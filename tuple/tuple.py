# Create a tuple to use as a key
tuple_key = ('apple', 'banana', 'cherry')

# Create a dictionary with the tuple as the key
fruits = {tuple_key: 'mixed fruit'}

# Access the value associated with the tuple key
print(fruits[tuple_key])

# Output: 'mixed fruit'
tuple = 1, 10, 100, 1000
a, b = b, a


import timeit
timeit.timeit([range(10)])