import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

def create_custom_hh(links, subtext):
    hh = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        score = subtext[index].select('.score')
        if len(score):
            points = int(score[0].getText().replace(' points', ''))
            if points > 100:
                hh.append({'title': title, 'href': href})
    return hh

pprint.pprint(create_custom_hh(links, subtext))