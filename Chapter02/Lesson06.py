from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
next_siblings = bs.find('table', {'id':'giftList'}).tr.next_siblings
for sibling in next_siblings:
    print(sibling)