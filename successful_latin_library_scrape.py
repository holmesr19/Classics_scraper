'''
successful_latin_library_scrape.py
a script of the code used to import the ovid texts
bancks holmes
'''
import requests
from bs4 import BeautifulSoup

url = "http://thelatinlibrary.com/ovid.html"
response = requests.get(url)
#print(response.text)
soup = BeautifulSoup(response.text, "html.parser")
links = soup.findAll("a")
link_txt = []
for link in links:
    link_txt.append(link.get('href'))

link_txt = link_txt[0:60]

for string in link_txt:
    new_url = "http://thelatinlibrary.com/" + string
    new_soup = BeautifulSoup(requests.get(new_url).text, "html.parser")
    filename =  string + ".txt"
    with open(filename, 'w') as file:
        file.write(str(new_soup.get_text()))

