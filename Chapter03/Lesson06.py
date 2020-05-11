from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import urllib.parse
import re

import arabic_reshaper
from bidi.algorithm import get_display

# html = urlopen("https://www.digikala.com/search/category-mobile-phone/")
# bs = BeautifulSoup(html, 'html.parser')
# links = bs.find('div', {'class': 'c-listing js-listing'}).find_all('a', href=re.compile('^(/product/)'))
# for link in links:
#     print(link['href'])
# u' '.join((agent_contact, agent_telno)).encode('utf-8').strip()
pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('https://www.digikala.com{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    links = bs.find_all('a', href=re.compile('^(/product/)'))
    for link in links:
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                quoted = urllib.parse.quote(newPage)
                getLinks(quoted)

getLinks('/search/category-mobile-phone/')

# pages = set()
# def getLinks(pageUrl):
#     global pages
#     html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
#     bs = BeautifulSoup(html, 'html.parser')
#     links = bs.find_all('a', href=re.compile('^(/wiki/)'))
#     for link in links:
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 #We have encountered a new page
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)
#
# getLinks('')

# /product/dkp-2645406/