import re

# Example string to search
example_string = "The quick brown fox jumps over the lazy dog fox."

# Example pattern to search for
example_pattern = r"fox"

# Example using findall()
# we use findall() to find all occurrences of fox in the string. This returns a list with one item: ['fox'].
matches = re.findall(example_pattern, example_string)
print(matches)
# Output: ['fox']

# Example using search()
# we use search() to find the first occurrence of fox in the string. 
match_object = re.search(example_pattern, example_string)
if match_object:
    print(match_object.group())
# Output: 'fox'

# Example using match()
# we use match() to search for fox at the beginning of the string. 
match_object = re.match(example_pattern, example_string)
if match_object:
    print(match_object.group())
else:
    print("No match at beginning of string")
# Output: "No match at beginning of string"


import re

string = "The quick brown fox jumps over the lazy dog"
pattern = r"^The\s+quick\s+brown"

match = re.search(pattern, string)
if match:
    print("Both words found")
else:
    print("One or both words not found")
