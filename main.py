import urllib.request
from bs4 import BeautifulSoup
import spacy
import json
import csv
import re
import usaddress
import logging


#load the language model instance in spacy
nlp =spacy.load('en_core_web_sm') 

def get_webpage(url : str )-> str:
    try:
        # Getting the webpage, creating a Response object.
        response = urllib.request.Request(url, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
        html = urllib.request.urlopen(response)
        html_bytes = html.read()
        page_html= html_bytes.decode("utf8")
        return page_html
    except:
        return None

def get_webpage_text(html : str )-> str:
# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(html, 'lxml')
    #Finding the text
    page_text = soup.text
    
    return page_text

def get_list(page_html)->list:
    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(page_html, 'lxml')
 
# # Extracting all the <a> tags into a list.
    a_tag = soup.findAll('a', {'class': '100link'})

    company_name_url_list=[]
    for name in a_tag:
        if name.text!="View From The Top Profile":
            company_name_url_list.append([name.text,name.get('href')])
    return company_name_url_list


def get_contact_page_link(html : str )-> list:
    contact_list=[]
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all('a'):
        try:
            link=tag.attrs['href']
            # link=tag.get('href')
            name=tag.text
            title=["Contact","Offices","about","contact"]
            for item in title:
                if item in name:
                    contact_list.append(link)
            # return contact_list
        except:
            link=tag.get('href')
            name=tag.text
            title=["Contact","Offices","about","contact"]
            for item in title:
                if item in name:
                    contact_list.append(link)
    contact_list=list(dict.fromkeys(contact_list))
    return contact_list


def get_location(text : str)-> list:
    address_list=[]
    location_list=[]
    patterns=[r'[0-9|A-Z|a-z ]*\n[A-Z|a-z ]*\n\t\t\t\t\t[A-Z|a-z]*[,]\s[A-Z]{2}\s[0-9]{5}',r'[0-9|A-Z|a-z]*\s[A-Z|a-z|0-9]*\s[A-Z|a-z|0-9]*[, ]\s[A-Z|a-z]*\s[0-9]*\n[A-Z|a-z\s]*[,]\s[A-Z]{2}\s[0-9]{5}',r'^\s[0-9]{3}\s[a-z|A-Z|0-9\s]*[,]\s[0-9|a-z|A-Z]*\s[a-z|A-Z]*\n[A-Z|a-z\s]*[, ]\s[A-Z]{2}\s[0-9]{5}',r'^[0-9a-zA-Z ]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]{5}\n\bUnited States|USA\b$',r'^[0-9]{3}[a-z|A-Z\s]*\s[a-z|A-Z]{2}.[A-Z|a-z]*\s[0-9]*[A-z|a-z|0-9]*[,]\s[A-Z]{2}\s[0-9]{5}$',r'^[a-z|A-Z|0-9]*[,]\s[A-z]{2}\s[0-9]{5}\r\n\bUnited States\b',r'[0-9]*\s[A-z].\s[a-z|0-9]*\s[A-Z|a-z]*.\n[A-Za-z]*\s[A-z|a-z]*[, ]\s[A-Z]{2}\s[0-9]{5}\n\bUSA\b']
    for pattern in patterns:
        find = re.findall(pattern,text.strip(), flags = re.MULTILINE)
        for item in find:
            item= re.sub(r'[^\x00-\x7f]',' ', item)
            item= re.sub(r'\n|\t|\r',' ', item)
            address_list.append(item)
    location_list=[item for item in address_list if item not in location_list]
    return location_list

def save_to_json(filename : str ,json_dict : dict)-> None:

     with open(filename, "w") as file_obj:
#write all the entites data in json
            file_obj.write(json.dumps(json_dict))
     

def json_to_csv_file(json_filename  : str ,csv_filename : str)-> None:
            # Opening JSON file and loading the data 
# into the variable data 
    with open(json_filename) as json_file: 
        data =json.load(json_file)
        temp=[]
        for i in data:
            temp.append({"company name":i,"location":data[i]})

        # field names  
        fields = ["company name","location"]  
        # writing to csv file  
        with open(csv_filename, 'w') as csvfile: 
            # creating a csv dict writer object  
            writer = csv.DictWriter(csvfile, fieldnames = fields)  
        
            # writing headers (field names)  
            writer.writeheader()  
        
            # writing data rows  
            writer.writerows(temp) 


if __name__ == '__main__':
    url = "http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"
    html= get_webpage(url)
    #print(html)
    #print("\n\n")
    company_list=get_list(html)
    #print(company_list)
    #print("\n\n")
    all_contact_list=[]
    for company in company_list[:10]:
        contact_list=[]
        url=company[1]
        html=get_webpage(url)
        if html==None:
            pass
        else:
            contact_page_list=get_contact_page_link(html)
            if len(contact_page_list):
                print("got contact page links for :"+company[0]+"\n")
                for item in contact_page_list:
                    if item.startswith('/'):
                        contact_list.append(company[1]+item)
                    else:
                        contact_list.append(item)
                all_contact_list.append(contact_list)
            else:
                logging.basicConfig(filename='company_url.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
                logging.info(company[0])
    print(all_contact_list,len(all_contact_list))
    count=0
    contact_link_list=["https://www.apple.com/contact/","https://www.aptaracorp.com/about-aptara/contact-us","https://act-on.com/contact-us/","https://www.acquia.com/about-us/contact","https://www.acrolinx.com/contact/","https://www.zoominsoftware.com/contact-us/","https://www.wochit.com/contact/"]
    for item in contact_link_list:
        count+=1
        print(count)
        page_html=get_webpage(item)
        page_text=get_webpage_text(page_html)
        print(get_location(page_text))
        
