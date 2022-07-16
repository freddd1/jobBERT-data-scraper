import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_description(web: BeautifulSoup) -> str:
    """
    Returns the description of the Job Title.
    :param web: BeautifulSoup object of the website.
    :return: description (string)
    """
    descriptions = web.findAll('div', attrs={'class': 'description'})
    for i, d in enumerate(descriptions):
        paragraphs = d.findAll('p')
        for j, p in enumerate(paragraphs):
            if i == 2 and j == 1:
                return p.text


def get_code(web: BeautifulSoup) -> str:
    """
    Returns the code of the Job Title.
    :param web: BeautifulSoup object of the website.
    :return: code (string)
    """
    descriptions = web.findAll('div', attrs={'class': 'code'})
    for i, d in enumerate(descriptions):
        paragraphs = d.findAll('p')
        return paragraphs[1].text


if __name__ == "__main__":
    columns = ['occupation', 'code', 'description']
    a = []
    meta_data = pd.read_csv('data/titles.test.csv')
    for url in meta_data['conceptUri']:
        redirected_url = 'https://esco.ec.europa.eu/en/classification/occupation?uri='
        r = requests.get(redirected_url + url)
        soup = BeautifulSoup(r.content, 'html5lib')
        occupation = str(soup.findAll('h3')[0].string).strip()
        code = get_code(soup)
        description = get_description(soup)
        row = [occupation, code, description]
        a.append(row)
        # break

    df = pd.DataFrame(a, columns=columns)
    df.to_excel("data/df.xlsx")
