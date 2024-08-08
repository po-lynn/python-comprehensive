import requests
"""
 <!DOCTYPE html>  
    <html>  
        <head>
            <title>Title on Browser Tab</title>
        </head>
        <body>
            <h1> Website Header </h1>
            <p> Some Paragraph </p>
        <body>
    </html>

"""
# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter 
# Note sometimes you need to run this twice if it fails the first time
res = requests.get("http://www.example.com")
# print(res)
# print(type(res))
# print(res.text)


import bs4
soup = bs4.BeautifulSoup(res.text,"lxml")
# print(soup)

# print(soup.select('title'))

title_tag = soup.select('title')
title_tag[0]

print(type(title_tag[0]))
print(title_tag[0].getText())