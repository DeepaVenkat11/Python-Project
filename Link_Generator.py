import requests
import time
from bs4 import BeautifulSoup
url=input("Enter a URL : ")
links=[]
website=requests.get(url)
website_text=website.text
soup=BeautifulSoup(website_text)
for link in soup.find_all('a'):
    links.append(link.get('href'))
for link in links:
    print(link)
    time.sleep(1)
print(len(links))
