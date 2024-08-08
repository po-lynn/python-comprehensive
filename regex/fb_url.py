

""""
import re
url = input("URL: ").strip()
matches = re.search(r"^https?://(?:www\.)?facebook\.com/(.+)$",url,re.IGNORECASE)
if matches:
    print(f'Hello, {matches.group(1)}')
    print(f'Hello, {matches.group(0)}')
"""

import re

text = "John Doe (jdoe@example.com)"
pattern = r"(\w+) (\w+) \((\w+@\w+\.\w+)\)"

match = re.search(pattern, text)

if match:
    name = match.group(1)
    email = match.group(3)
    email_username = email.split("@")[0]
    email_domain = email.split("@")[1]
    
    print("Name:", name)
    print("Email:", email)
    print("Email username:", email_username)
    print("Email domain:", email_domain)
else:
    print("No match found")
