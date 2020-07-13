import requests
from bs4 import BeautifulSoup
import re
import usaddress
 

url="https://www.acquia.com/about-us/contact"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')
page_text = soup.text

address_list=[]
detail_list=[]
find = re.findall(r'^[0-9a-zA-Z ]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]{5}\n\bUnited States|USA\b$',page_text, flags = re.MULTILINE)
for item in find:
    item= re.sub(r'[^\x00-\x7f]',' ', item)
    item= re.sub(r'\n',' ', item)
    address_list.append(item)
    detail_list.append(usaddress.parse(item))
for item in detail_list:
    details_dict={}
    for inner_item in item:
        if inner_item[1] not in details_dict:
            details_dict[inner_item[1]]=inner_item[0]
        else:
            already_value= details_dict[inner_item[1]]
            if already_value!=inner_item[0]:
                details_dict[inner_item[1]]=already_value+" "+inner_item[0]
    print("\n"+str(details_dict)+"\n")

