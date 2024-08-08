import re


"""
In summary, findall() is used to find all matches of a regular expression in the input string,
while match() is used to find the first match of a regular expression at the beginning of the input string.
"""
# define the regular expression pattern
pattern = r"\d+"

# define the input string
text = "I have 3 apples and 5 oranges."

# find all matches of the pattern in the input string
matches = re.findall(pattern, text)

# print the matches
print(matches)

import re

# define the regular expression pattern
pattern = r"\d+"

# define the input string
text = "4 apples and 5 oranges."

# try to match the pattern at the beginning of the input string
match = re.match(pattern, text)

# print the match
if match:
    print("Match found:", match.group())
else:
    print("No match found.")

