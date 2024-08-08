import itertools

# Generate a full permutation of ABCD
# for value in itertools.permutations('ABCD'):
#     print(value)

# Generate ABCDE five selection three combinations
for value in itertools.combinations('ABCDE', 3):
    print(value)


# create a list of numbers
numbers = [1, 2, 3, 4, 5]

# iterate over the list and print all possible combinations of 2 numbers
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        print((numbers[i], numbers[j]))



# Produces the Cartesian product of ABCD and 123
# for value in itertools.product('ABCD', '123'):
#     print(value)

# Generate an infinite loop sequence of ABC
it = itertools.cycle(('A', 'B', 'C'))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))