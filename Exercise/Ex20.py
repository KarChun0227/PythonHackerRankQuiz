import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(base_url)
r_html = r.text

soup = BeautifulSoup(r_html)

with open('file_to_save.txt', 'w') as open_file:
    open_file.write(soup.get_text())
    open_file.close