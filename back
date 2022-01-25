import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(html_text, 'lxml')

active = soup.find('li', class_ = 'bg-blue').text

cases = []


cases.append(active.split())

inc = cases[0][2]
increase = inc[1:len(inc)-1]

print(f"The total number of active cases in India is {cases[0][1]}\n({increase} increase from yesterday)")

vaccine_stats = []

vaccine = soup.find('div', class_ = 'col-xs-8 site-stats-count sitetotal').text

vaccine_stats.append(vaccine.split())
new = vaccine_stats[0][4]
new_vaccines = new[1:len(new)-1]

print(f"Total number of vaccinations registered : {vaccine_stats[0][3]}")
print(f"{new_vaccines} vaccinations registered today!")
