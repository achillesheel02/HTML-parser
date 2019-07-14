import requests
from bs4 import BeautifulSoup
url='http://jiji.co.ke/all-businesses-orgs/6/all'
content = requests.get(url)
soup = BeautifulSoup(content.text,"html.parser")
with open('names.txt','a') as f:
    for name in soup.find_all('span','orgname'):
        f.write(name.string+'\n')
