from bs4 import BeautifulSoup
import requests
import re
import csv
import json
import spacy

#load the language model instance in spacy
nlp =spacy.load('en_core_web_sm')

#function to get html content of web page using requests module
def get_webpage(url : str )-> str:
    try:
        response = requests.get(url)
        page_html=response.text
        return page_html
    except:
        return None

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

#
def get_contact_page_link(html : str )-> list:
    contact_page_link=[]
    company_name_url=get_list(html)
    for item in company_name_url:
        try:
            name=item[0]
            url=item[1]
            page_html=get_webpage(url)
            contact_link=[]
            soup = BeautifulSoup(page_html, "lxml")
            a_tag=soup.findAll('a')
            link_only=[]
            for item in a_tag:
                link_only.append(item.get('href'))
            pattern=["contact","about"]
            for link in link_only:
                for item in pattern:
                    if re.search(item,link):
                        if link.startswith('http'):
                            contact_link.append(link)
                        else:
                            contact_link.append(url+link)
            contact_page_link.append([name,contact_link])
            print("got contact of name : ",name)
        except:
            print("coudnt get for ",name)
    return contact_page_link

#
def get_location(text : str)-> list:
    loc_list=[]
    doc = nlp(text)
#itrate each entity and append in list 
    for ent in doc.ents:
            if "GPE" in ent.label_ :
                loc_list.append(ent.text)
#remove repeated name and their entity 
    com_loc_list= [] 
    [com_loc_list.append(x) for x in loc_list if x not in com_loc_list ]

    return com_loc_list

def save_to_json(filename : str ,json_dict : dict)-> None:
    with open(filename, "w") as file_object:
        #write all the entites data in json
        file_object.write(json.dumps(json_dict, sort_keys=False, indent=2, separators=(',', ': ')))
    return None

def json_to_csv_file(json_filename  : str ,csv_filename : str)-> None:
    with open(json_filename) as json_file: 
        data = json.load(json_file)
    data_file = open(csv_filename, 'w')
    csv_writer = csv.writer(data_file)
    
    for item in data:
        csv_writer.writerow(item)
    # create the csv writer object 
    # csv_writer = csv.writer(data_file) 


#url
url="http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"

#calling function to get page_html
page_html=get_webpage(url)
filename='data.json'

# print(page_html)

# #calling function to get webpage visible text
# page_text=get_webpage_text(page_html)
# print(page_text)
# #calling function to get list containing company name & url
#company_name_url=get_list(page_html)
# print(company_name_url)
#print(get_contact_page_link(page_html))
# to get list conataining company name and contact url
comName_contactUrl_list=get_contact_page_link(page_html)
comp_dict=[]
for company in comName_contactUrl_list:
     
     name=company[0]
     url=company[1]
     text=get_webpage_text(url)
     loction_list=get_location(text)
     comp_dict[name]=loction_list
save_to_json(filename,comp_dict)
json_to_csv_file(json_filename csv_filename)
    
