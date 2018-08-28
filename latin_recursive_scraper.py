'''
Author: Bancks Holmes
File: Latin_recursive_Scraper.py
Usage: This program scrapes the text from each page of 
thelatinlibrary.com and stores it as its own text file.
In the future, I plan that it should accept a command line
argument that is a url and it will clone the file structure 
of the desired site.
'''

import requests
from bs4 import BeautifulSoup
import time


headers = {
'User-Agent' : 'Robert Holmes',
'From' : 'holmesr19@mail.wlu.edu'
}

cache = []
link_text = []
blacklist_exts = ['index.html', 'classics.html']

def get_ext(url):
    '''accepts a url as a string and works backwards to 
    determine the extension of the url, which it returns 
    as a string '''
    ext = ""
    for char in reversed(url):
        if char != '/':
            ext = char + ext
        else:
            return ext

def good_ext(ext):
    '''accepts a extension as a string argument and 
    returns false if that string is in the blacklist, 
    true if it is not'''
    if ext in blacklist_exts:
        return False
    else:
        return True

def new_url(url):
    '''accepts url as a string argument and 
    returns false if that string is in the cache, 
    true if it is not'''
    if url in cache:
        return False
    else:
        return True

def build_url(ext):
    '''concatenates the extension to the latin library
     index page
     This will need to be revised to accept CLI argument
     when '''
    return "https://thelatinlibrary.com/" + ext

def name_file(url):
    '''names the file using the url'''
    return #url sliced after latinlibrary.com


def write_file(fn, text):
    '''accepts a filename and the text to write to the
     file and opens or creates the file, writes the text
      and closes the file'''
    pass

def make_dict(name, keys, values):
    '''accepts a list of keys and values and writes them
    into a dictionary which it returns.'''
    name = {}

def make_srtuct_file(dict):
    '''writes the struct file, which visualizes the structure of the 
    scraped website. '''
    open('struct.txt', w) as struct
    for key in dict:
        struct.write(key)
        '''for value:
            write -> value 
            if type(value)== dict, recurse'''



def recursive_scrape(url):
    '''This recursive function is effectively a depth-first
     search of the filesystem containing the text to be 
     scraped. It builds a list of links on the top level
     page, then visits the first link on that page that links
     to another file within the filesystem. '''
    time.sleep(5)
    print("recursive_scrape receiving url: ", url)
    try:
        page = requests.get(url) #this could be the init for a recursive_scraper object
        p_soup = BeautifulSoup(page.text, "html.parser")
        p_links = p_soup.find_all("a")
        link_text = []    
        links = []
        for item in p_links:
            txt = item.string
            if txt != None:
                link_text.append(url + txt)
                link = item.get('href')
                if link[0] != '#':
                    new_link = build_url(link)
                    print("new link: ", new_link)
                    if new_url(new_link):
                        cache.append(new_link)
                        #print(cache)
                        recursive_scrape(new_link)
                else:
                    file_name = "~/documents/research/" + url + '.txt'
                    latin_text = p_soup.stripped_strings
                    open(file_name, 'w')
                    file_name.write(latin_text)
                    print(file_name, " written")
                    file_name.close()
    except ValueError:
        print("Invalid URL: ", url)

                

    
def main():


    '''lib = requests.get("http://www.thelatinlibrary.com/indices.html", headers = headers)
    soup = BeautifulSoup(lib.text, "html.parser")   #brings the html into the current session as text

    page_links = soup.find_all("a")           #finds all the <a> tags in the BeautifulSoup object
    bottom_table = soup.find(cellpadding = "0")     #supposedly finds and gets rid of all the footer
    bottom_table.decompose()                                #<a> tags, but theyre still in the author names list...

    for item in page_links:      #SHOULD make a list of each authors name and a list with the link to his page..
        text = item.string
        if text != None:
                link_text.append(text)
                link = item.get('href')
                if link[0] == '/':
                    cache.append("http://thelatinlibrary.com" + link)
                else:
                    cache.append("http://thelatinlibrary.com/" + link)'''
    
    cache.append("http://www.thelatinlibrary.com/indices.html")
    for item in cache:
        #what if I just made the first item in the cache the input from CLI?
        #also need a way to enter blacklist values
        print("main passing url: ", item)
        recursive_scrape(item)


            
if __name__ == "__main__":
    main()

##to-do:
##    investigate and get rid of the empty lists at the end of names DONE
##    make names a list of strings instead of a list of lists DONE
##    figure out how to get a list of the href attributes DONE

##  incorporate blacklist
##  don't add '/' if one / already exists at the beginning of the extension
## make cache a set

######    drill down into each page, making sure to note the structure and when
#####      only href = # links remain, copy all the text
######    make a log file that catalogs anything abnormal that happens on each request (cato etc)
###### write pseudocode to nail down structure and go from there

#need to check operation of file writing syntax, move into its own function(s?)
#also write dictionaries to text files

#un-visitable sites are identified by those not beginning with the same 
#domain as the current page - 'do-not-visit- function

#should be refactored so that info is scraped and saved as a scraper object
#and then sent to analyzer object for analysis, possibly then visualizer 
#object afterwards

