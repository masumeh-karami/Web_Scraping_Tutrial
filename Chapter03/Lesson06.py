from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import urllib.parse

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('https://www.digikala.com{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.find_all('a', href=re.compile('^(/product/)'))
    for link in links:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                newurl = urllib.parse.quote(newpage)
                getLinks(newurl)

getLinks('/search/category-mobile-phone/')
