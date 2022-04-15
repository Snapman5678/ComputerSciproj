import requests
from bs4 import BeautifulSoup


def active_covid(soup: BeautifulSoup):
    ac_cases = soup.find('li', class_='bg-blue').text.split()
    return 'Active Cases:', ac_cases[1]


def vaccinations(soup: BeautifulSoup):
    vaccine = soup.find('div', class_='col-xs-8 site-stats-count sitetotal').text.split()
    return 'Total Vaccinations:', vaccine[3], 'New Vaccinations:', vaccine[4].lstrip("`(").rstrip(")'")


def covid_deaths(soup: BeautifulSoup):
    deaths = soup.find('li', class_='bg-red').text.split()
    return 'Total Deaths:', deaths[1], 'New Deaths:', deaths[2].lstrip("`(").rstrip(")'")


def all_cases():
    data = requests.get('https://www.mygov.in/covid-19').text
    count = BeautifulSoup(data, 'html.parser').find('div', class_='iblock t_case') \
        .find('span', class_='icount') \
        .text
    return 'Total Cases:', count
