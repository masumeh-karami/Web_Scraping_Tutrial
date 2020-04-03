from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError


try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The server could not found!')
else:
    bs = BeautifulSoup(html, 'html.parser')
try:
    title = bs.body.h1
except AttributeError as e :
    print('Tag was not found!')
else:
    if title == None:
        print('Tag was not found!')
    else:
        print(title)