import requests
from bs4 import BeautifulSoup
import re
 

url="https://www.acquia.com/about-us/contact"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'lxml')
page_text = soup.text
#print(page_text)
search = re.search(r"^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$",page_text)
print(search) 
match = re.match(r"^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$",page_text) 
print(match)
find = re.findall(r"^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$",page_text)
print(find) 



#tried the same using text directly from page:"https://www.acquia.com/about-us/contact"

text="""
Skip to main navigation

Information for:
DEVELOPERS
PARTNERS

ENGLISH
SUPPORT
LOGIN
REQUEST A DEMO
SOLUTIONS
PRODUCTS
RESOURCES
ABOUT
CONTACT US

CONTACT US
Contact us to learn more about the Acquia Platform.
Learn which Acquia solutions work best for you
First Name
Last Name
Email Address
Company
Industry
Job Title
Job Function
Job Level
Phone Number
Annual Revenue
Country
Comments
How did you hear about us?
Yes, I would like to receive updates and information about Acquia's products, events, webinars, and more. I understand I can unsubscribe at any time.
Our Offices
 

Boston, MA

53 State Street, 10th Floor
Boston, MA 02109
United States
Phone: 888-922-7842

U.S. Locations
Austin, Texas
600 Congress Ave
Austin, TX 78701
United States

Boston, MA
53 State Street, 10th Floor
Boston, MA 02109
United States

Phone: 888-922-7842
Portland, Oregon
1120 NW Couch St. Suite 550
Portland, OR 97209
United States

Santa Clara, CA
451 El Camino
Real Suite 235
Santa Clara, CA 95050
United States

Washington, D.C.
1775 Tyson’s Blvd
McLean, VA 22102
United States

International Locations
Brighton, UK
100/101 Queens Road
2nd Fl
Brighton
BN1 3XF
United Kingdom

Brisbane, Australia
310 Edward St
Brisbane City QLD 4000
Australia

Munich, Germany
Erika-Mann-Str. 53
80636 Munich
Germany

Paris, France
7 rue Meyerbeer
75009 Paris
France

Pune, India
Cerebrum B3, Kalyani Nagar
4th Floor, Office No. 4
Pune 411004
Maharashtra
India

Phone: +91 20 7127 9046
Reading, UK
The White Building, Third Floor
33 Kings Road
Reading
RG1 3AR
United Kingdom

Phone: +44 1865 520 010
Sydney, Australia
2 Elizabeth Plaza, Level 10
North Sydney NSW 2060
Australia

Phone: +61.2.8015.2576
Tokyo, Japan
2-24-12 Shibuya, Shibuya-ku
WeWork Shibuya Scramble Square 39F
Shibuya-ku, Tokyo
150-6139
Japan

Toronto, Canada
111 George Street, Suite 201
Toronto ON M5A 2N4
Canada

Phone: 647-953-4270
Acquia
53 State Street, 10th Floor
Boston, MA 02109 
888-922-7842

CONTACT US
COMPANY
Case Studies
Acquia Engage
Engage Awards
Careers
Newsroom
RESOURCES
Developer Center
Ideas & Publications
Webinars
Drupal 9
Product Documentation
Copyright © 2020 Acquia, Inc. All Rights Reserved. Drupal is a registered trademark of Dries Buytaert.
Legal
Security Issue?
"""
search = re.search(r'^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$',text)
print(search) 
match = re.match(r'^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$',text) 
print(match)
find = re.findall(r'^[0-9a-zA-Z-\s]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]*\n[A-za-z0-9]*\s[A-za-z0-9]*$',text)
print(find) 
