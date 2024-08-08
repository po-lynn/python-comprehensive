# Create a two-dimensional list
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Calculate the sum of each row
row_sums = []
for row in my_list:
    row_sum = sum(row)
    row_sums.append(row_sum)
print(row_sums)  # Output: [6, 15, 24]

# Transpose the list (swap rows and columns)
transposed_list = [[my_list[j][i] for j in range(len(my_list))] for i in range(len(my_list[0]))]
print(transposed_list)  # Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Find the maximum value in the list
max_value = my_list[0][0]
for row in my_list:
    for value in row:
        if value > max_value:
            max_value = value
print(max_value)  # Output: 9


