import timeit

# Using a list
list_setup = '''
my_list = [1, 2, 3, 4, 5]
'''
list_time = timeit.timeit(list_setup)

# Using a tuple
tuple_setup = '''
my_tuple = (1, 2, 3, 4, 5)
'''
tuple_time = timeit.timeit(tuple_setup)

print(f'List time: {list_time}')
print(f'Tuple time: {tuple_time}')

str = 'hello, world'
print("wo" in str)