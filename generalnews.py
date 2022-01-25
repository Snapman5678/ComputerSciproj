import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://timesofindia.indiatimes.com/world').text
soup = BeautifulSoup(html_text, 'lxml')
head = soup.find('div', class_ = 'top-newslist')

titles = []
links = []

for title in head.find_all('a'):
    headline = title.get('title')
    titles.append(headline)

for link in head.find_all('a'):
    a = 'https://timesofindia.indiatimes.com'+link.get('href')
    links.append(a)

length = len(titles)


with open("news.txt",'w') as f:
    for i in range (len(titles)-1):
        n = str(i + 1)+')'
        f.write(n)
        f.write('TITLE:'+titles[i+1]+'\n\r')
        f.write(' '+'LINK:'+links[i+1]+'\n\r')
        f.write('\n\r')
