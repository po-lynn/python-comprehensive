def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = [square(n) for n in numbers]

print(squared_numbers) # Output: [1, 4, 9, 16, 25]

# ========================================
def square(n):
    return n ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

print(list(squared_numbers)) # Output: [1, 4, 9, 16, 25]
