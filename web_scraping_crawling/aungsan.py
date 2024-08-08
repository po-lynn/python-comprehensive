import requests
import bs4
res = requests.get('https://en.wikipedia.org/wiki/Aung_San')


# Create a soup from request
soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup)
# note depending on your IP Address, 
# this class may be called something different
soup.select(".toctext")