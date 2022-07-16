import requests
from bs4 import BeautifulSoup

URL = "https://esco.ec.europa.eu/en/classification/occupation?uri=http%3A%2F%2Fdata.europa.eu%2Fesco%2Foccupation%2F47e81c7f-2d04-4a60-a8ff-9913c36d8344"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

descriptions = soup.findAll('div', attrs={'class': 'description'})


for d in descriptions:
    paragraphs = d.findAll('p')
    for i, p in enumerate(paragraphs):
        print(i, p.text)