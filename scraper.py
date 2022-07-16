import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import time

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


def get_atr_label(web: BeautifulSoup) -> str:
    """
    Returns the alternative label of the Job Title.
    :param web: BeautifulSoup object of the website.
    :return: alternative label (string)
    """
    descriptions = web.findAll('div', attrs={'class': 'alternative-labels'})
    alter_labels = []
    for i, d in enumerate(descriptions):
        paragraphs = d.findAll('p')
        for j, p in enumerate(paragraphs):
            alter_labels.append(p.text)
    return alter_labels


def get_skills(web: BeautifulSoup) -> str:
    """
    Returns the skills of the Job Title.
    :param web: BeautifulSoup object of the website.
    :return: alternative label (string)
    """
    descriptions = web.findAll('div', attrs={'class': 'essential-skills-list'})
    skills = []
    for i, d in enumerate(descriptions):
        paragraphs = d.findAll('a')
        for j, p in enumerate(paragraphs):
            skills.append(p.text)
    return skills



if __name__ == "__main__":
    columns = ['occupation', 'code', 'description', 'alternative_labels', 'skills']
    a = []
    meta_data = pd.read_csv('data/titles.test.csv')
    for url in tqdm(meta_data['conceptUri'], desc='tqdm() Progress Bar'):
        redirected_url = 'https://esco.ec.europa.eu/en/classification/occupation?uri='
        r = requests.get(redirected_url + url)
        soup = BeautifulSoup(r.content, 'html5lib')
        try:
            occupation = str(soup.findAll('h3')[0].string).strip()
            code = get_code(soup)
            description = get_description(soup)
            alternative_labels = get_atr_label(soup)
            skills = get_skills(soup)
            row = [occupation, code, description, alternative_labels, skills]
            a.append(row)
        except:
            print('Skipping-{} '.format(url))
        # break

    df = pd.DataFrame(a, columns=columns)
    df.to_excel("data/df.xlsx")
