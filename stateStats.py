import requests
from bs4 import BeautifulSoup


def stateWise():
    data = ['Sl', 'STATE', 'TOTAL', 'ACTIVE', 'CURED', 'DEATHS']
    html_text = requests.get('https://prsindia.org/covid-19/cases').text
    soup = BeautifulSoup(html_text, 'html.parser')
    table = soup.find('table', class_='table table-striped table-bordered')
    body = table.find('tbody')
    state_data = body.find_all('td')
    for i in state_data:
        a = i.text
        data.append(a)
    data = [data[i * 6: (i + 1) * 6] for i in range((len(data) + 6 - 1) // 6)]
    return data
