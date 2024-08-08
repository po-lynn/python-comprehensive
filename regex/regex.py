import re

# pattern = ".+@."
# string = "I have a cat cat.@"

# match = re.search(pattern, string)
# if match:
#   print("Match found!")
# else:
#   print("Match not found.")
import re

string = "The quick brown fox"

# Check if the string starts with "The"
if re.match("^The", string):
  print("The string starts with 'The'")


import re

pattern = r"ca?t"

if re.search(pattern, "catcat"):
    print("Match found!")

# if re.search(pattern, "ct"):
#     print("Match found!")

# if re.search(pattern, "caat"):
#     print("Match found!")
import re

# pattern = r"(\d+): (\w+)"
# input_str = "1: apple"
# match = re.search(pattern, input_str)
# if match:
#     # Get the value of the first group
#     number = match.group(1)
#     word = match.group(2)
#     print(f"Number: {number}, Word: {word}")


# name = input("What's your name? ").strip()
# if matches := re.search(r"^(.+), ?(.+)$",name):
#   name = matches.group(1) + " " + matches.group(2)

# print(f"hello, {name}")
# https://www.facebook.com/lyn.drupal

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?facebook\.com/(.+)$",url,re.IGNORECASE)
if matches:
  print(f'Hello, {matches.group(1)}')