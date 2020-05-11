from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


html = urlopen('https://en.wikipedia.org/wiki/Ali_Daei')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id': 'bodyContent'}).find_all(
        'a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

import datetime
import random

random.seed(datetime.datetime.now())
def getLinks(wikiUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(wikiUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).find_all('a',
        href=re.compile('^(/wiki/)((?!:).)*$'))
links = getLinks('/wiki/Ali_Daei')
while len(links) > 0:
    newPage = links[random.randint(0, len(links)-1)].attrs['href']
    print(newPage)
    links = getLinks(newPage)