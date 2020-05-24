from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse
import re


pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('https://www.digikala.com{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.find_all('a', href=re.compile('^(/product/)'))
    try:
        title = bs.h1.get_text()
        print(title)
        attributes = bs.find('div' , { 'class' :'c-product__params js-is-expandable'}).find('ul').find_all('li')
        for attribute in attributes:
            print(attribute.get_text().strip())

    except AttributeError:
        print('This page is missing something! Continuing.')

    for link in links:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newpage = link.attrs['href']
                print('_'*200)
                print(newpage)

                pages.add(newpage)
                newurl = urllib.parse.quote(newpage)
                getLinks(newurl)

getLinks('/search/category-mobile-phone/')