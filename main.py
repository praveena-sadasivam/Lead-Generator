import urllib.request
from bs4 import BeautifulSoup
import json
import csv
import re
import logging
from regex_expression import patterns1,patterns2
from contact_list import contact_link_list


#function to get html content using urllib module 
def get_webpage(url : str )-> str or None:
    try:
        # Getting the webpage, creating a Response object.
        response = urllib.request.Request(url, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
        html = urllib.request.urlopen(response)
        html_bytes = html.read()
        page_html= html_bytes.decode("utf8")
        return page_html
    except:
        return None


#function to get visible text of web page using BeautifulSoup
def get_webpage_text(html : str )-> str:
    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(html, 'lxml')
    #Finding the text
    page_text = soup.text
    
    return page_text


#function to get list of companies along with url
def get_list(page_html)->list:
    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(page_html, 'lxml')
 
    # Extracting all the <a> tags into a list.
    a_tag = soup.findAll('a', {'class': '100link'})

    company_name_url_list=[]
    for name in a_tag:
        if name.text!="View From The Top Profile":
            company_name_url_list.append([name.text,name.get('href')])
    return company_name_url_list

#function to get contact page links of each company as list
def get_contact_page_link(html : str )-> list:
    contact_list=[]
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all('a'):
        
        try:
            if tag.has_attr('href'):
                link=tag.attrs['href']
                title=["office","about","contact","locations"]
                for item in title:
                    if item in link:
                        contact_list.append(link)
            
        except:
            link=tag.get('href')
            if len(link)!=0:
                title=["office","about","contact","locations"]
                for item in title:
                    if item in link:
                        contact_list.append(link)
    contact_list=list(dict.fromkeys(contact_list))
    return contact_list

#function to get address of each company using regex expression
def get_location(text : str)-> list:
    address_list=[]
    for pattern in patterns1:
        find = re.findall(pattern,text.strip(), flags = re.MULTILINE)
        for item in find:
            item= re.sub(r'[^\x00-\x7f]',' ', item)
            item= re.sub(r'\n|\t|\r',' ', item)
            if len(item)>4 and item.isdigit()==False:
                
                item=" ".join(item.split())
                address_list.append(item)
    address_list=list(dict.fromkeys(address_list))
    if len(address_list)==0:
        address_list=[]
        for pattern in patterns2:
            find = re.findall(pattern,text.strip(), flags = re.MULTILINE)
            for item in find:
                item= re.sub(r'[^\x00-\x7f]',' ', item)
                item= re.sub(r'\n|\t|\r',' ', item)
                    
                if len(item)>4 and item.isdigit()==False:
                    item=" ".join(item.split())
                    address_list.append(item)
        print("Match found in pattern 2")
        
        address_list=list(dict.fromkeys(address_list))
    else:
        print("Match found in pattern 1")
    
    return address_list

#function to store address in json file
def save_to_json(filename : str ,json_dict : dict)-> None:
    with open(filename, "w") as file_obj:
        #write all the data in json
        file_obj.write(json.dumps(json_dict, sort_keys=False, indent=2, separators=(',', ': ')))
        print("\nSuccessfully data saved to json\n ")
        print("check ",filename)
        print("\n")
    return None


#function to convert json into csv
def json_to_csv_file(json_filename  : str ,csv_filename : str)-> None:
    # Opening JSON file and loading the data 
    with open(json_filename) as json_file: 
        data =json.load(json_file)
        
         # writing to csv file  
        with open(csv_filename, 'w') as csvfile: 

            # field names  
            fields = ["Company","Addresses"]  
       
            # creating a csv writer object  
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(fields) 
            for item in data:
                add=" | ".join(data[item])
                s=[item,add]
              
               # writing data rows  
                writer.writerow(s)
            
            print("Successfully convert json into csv \n")
            print("check ",csv_filename)
            print("\n")
    return None


if __name__ == '__main__':
    no_html=[]
    in_log_file=[]
    #Create and configure logger
    log_file_name="no_contact.log"
    logging.basicConfig(filename=log_file_name,format='%(asctime)s %(message)s',filemode='w')
    #Creating an object 
    logger=logging.getLogger()
    #Setting the threshold of logger to DEBUG 
    logger.setLevel(logging.DEBUG) 
    logger.info("List of companies that has no contact details") 


    #starts from here
    url = "http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"
    #getting html content
    html= get_webpage(url)
    company_list=get_list(html)
    print("\nlist of 100 company with its url: ")
    print("\n\n")
    #getting company list
    print(company_list)
    print("\n\n")
    print("lenth of company list : ",len(company_list))
    print("\n\n")
    #getting contact list of each company 
    all_contact_list=[]
    #testing for 1st ten companies
    print("getting contact link : ")
    for company in company_list:
        contact_list=[]
        url=company[1]
        html=get_webpage(url)
        if html != None:
            contact_page_list=get_contact_page_link(html)
            if len(contact_page_list):
                print("got contact page links for : "+company[0]+"\n")
                for item in contact_page_list:
                    if item!= None and item.startswith('/'):
                        contact_list.append(company[1]+item)
                    else:
                        contact_list.append(item)
                all_contact_list.append(contact_list)
            else:
                print("no contact page for : "+company[0]+"\n")
                print("company name and url stored in ",log_file_name)
                print("\n")
                logger.setLevel(logging.DEBUG) 
                logger.info(company[0])
                logger.info(company[1])
                in_log_file.append(company[1]) 

        else:
            print("could not get html content for : "+company[0]+"\n")
            no_html.append(company[1])
            pass

    print("contact page links of companies\n")
    print(all_contact_list)
    print("\n")
    print("No of companies that has contact link : ",len(all_contact_list))
    print("\n")
    print("list of companies getting some error while requesting for html content of web page\n")
    print(no_html)
    print("\n")
    print("No of companies whose html content was not available : ",len(no_html))
    print("\n")
    print("No of companies which has no contact details, and are saved in log file: ",len(in_log_file))
    print("\n")
    
    
    print("now getting address of few companies :")
    print("\n\n")
    #taking a list of companies that has proper contact page link and located in USA,Since usaddress module will be used for parsing address    
    final_dict={}
    for item in contact_link_list:
        company_name=item[0]
        contact_link=item[1]
        page_html=get_webpage(contact_link)
        if page_html!= None:
            page_text=get_webpage_text(page_html)
            #to get address of each company
            location_list=get_location(page_text)
            final_dict.update({company_name:location_list})
            print("company name: ",company_name)
            print("\naddress list :\n")
            print(location_list)
            print("\n")

        else:
            print("could not get html content of ",company_name)
            print("\n")
            pass
    print("\n")
    print("found address of "+str(len(contact_link_list))+" companies.\n")
    print(final_dict)
    print("\n")
    filename="company_details.json"
    save_to_json(filename,final_dict)
    json_to_csv_file(filename,"company_details.csv")

        
