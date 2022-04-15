import requests
from bs4 import BeautifulSoup


def news():
    html_text = requests.get('https://timesofindia.indiatimes.com/world').text
    soup = BeautifulSoup(html_text, 'html.parser')
    return [line.text for line in soup.find('div', class_='top-newslist').find_all('a')][1:]
