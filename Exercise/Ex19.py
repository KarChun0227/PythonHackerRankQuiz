import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
r_html = r.text

soup = BeautifulSoup(r_html)

print(soup.get_text())