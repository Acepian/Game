# here I import BeautifulSoup package to help me organize web data
#we are using urlib and open to request url

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#input "url" request link
my_url='https://www.newegg.com/p/pl?d=graphics+card&N=100007709&isdeptsrh=1'

# opening connection, grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()

#closing the connection
uClient.close()
