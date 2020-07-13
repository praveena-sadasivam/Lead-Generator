import requests
from bs4 import BeautifulSoup
import re
 
url="https://www.acquia.com/about-us/contact"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')
page_text = soup.text
#print(page_text)
search = re.search(r'^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$',page_text)
print(search) 
match = re.match(r'^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$',page_text) 
print(match)
find = re.findall(r'^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$',page_text)
print(find) 
