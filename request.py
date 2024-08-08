# import requests
# response = requests.get('https://www.example.com')
# print(response.text)

# The response object that is returned contains the HTTP response from the server, including the status code, headers, and the content of the response (if any). You can access these properties using the following attributes:

# response.status_code: The HTTP status code of the response (e.g. 200 for a successful request)
# response.headers: A dictionary of HTTP headers
# response.content: The content of the response as bytes
# response.text: The content of the response as a Unicode string
# You can also use the requests.post() function to send an HTTP POST request to a specified URL, and the requests.put() function to send an HTTP PUT request. There are also functions for sending other HTTP methods, such as DELETE and PATCH.

# In addition to the basic request functions, the requests module also provides several other useful features, such as the ability to add headers and query parameters to requests, and to handle cookies and authentication.

import requests

# Make the API request
response = requests.get('https://dummyjson.com/products/1')

# # Check if the request was successful
if response.status_code == 200:
    # Convert the response to a JSON object
    data = response.json()
    # Do something with the data
    print(data)
else:
    print('API request failed')

# print(data['title'])


response = requests.get('https://dummyjson.com/products')
# Check if the request was successful
if response.status_code == 200:
    # Convert the response to a JSON object
    data = response.json()
    # Do something with the data
    # print(data)
else:
    print('API request failed')
# {
#   "name": "John",
#   "age": 30,
#   "isEmployed": true
# }
for result in data['products']:
    print(result['title'])