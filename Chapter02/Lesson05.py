from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')
children_content = bs.find('table', {'id':'giftList'}).children
descendant_content = bs.find('table', {'id':'giftList'}).descendants
# descendant_list = list(descendant_content)
# print(descendant_list[20])

for child in descendant_list:
    print(child)

