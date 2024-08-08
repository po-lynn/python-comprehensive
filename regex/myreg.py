import re


# Define a pattern that matches the letter 'a' exactly three times
pattern = r'a{3}'

# # Test the pattern against some strings
# print(re.match(pattern, 'aaa')) # Output: <re.Match object; span=(0, 3), match='aaa'>
# print(re.match(pattern, 'aab'))  # Output: None
# print(re.match(pattern, 'aaaa')) # Output: <re.Match object; span=(0, 3), match='aaa'>


# import re

# Define a pattern that matches a string of digits that has between 3 and 5 characters
pattern = r'^\d{3,5}$'

# Test the pattern against some strings
# print(re.match(pattern, '12'))        # Output: None
# print(re.match(pattern, '123'))       # Output: <re.Match object; span=(0, 3), match='123'>
# print(re.match(pattern, '1234'))      # Output: <re.Match object; span=(0, 4), match='1234'>
# print(re.match(pattern, '12345'))     # Output: <re.Match object; span=(0, 5), match='12345'>
# print(re.match(pattern, '123456'))    # Output: None

# Define a pattern that matches a string that does not contain any vowels
pattern = r'[^aeiou]'
print(re.match(pattern, 'ogd'))

