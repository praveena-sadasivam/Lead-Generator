from bs4 import BeautifulSoup
import requests

#function to get html content of web page using requests module
def get_webpage(url : str )-> str:
    response = requests.get(url)
    page_html=response.text
    return page_html

#function to get visible text from each page using beautiful soup module
def get_webpage_text(html : str )-> str:
    soup = BeautifulSoup(html, "lxml")
    page_text=soup.text
    return page_text

#function to get company name and url as a list
def get_list(page_html)->list:
    soup = BeautifulSoup(page_html, "lxml")
    content=soup.findAll('a',{'class':'100link'})
    company_name_url=[]
    for item in content:
        if item.text!="View From The Top Profile":
            company_name_url.append([item.text,item.get('href')])
    return company_name_url
#url
url="http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"

#calling function to get page_html
page_html=get_webpage(url)
print(page_html)

#calling function to get webpage visible text
page_text=get_webpage_text(page_html)
print(page_text)


#calling function to get list containing company name & url
company_name_url=get_list(page_html)
print(company_name_url)

