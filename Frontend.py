from tkinter import * 
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("COVID-care")
root.geometry('600x700')
root.configure(background='#5d8a82')

# entry for state name

html_text = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(html_text, 'html.parser')


# finding active cases

def active_covid():
    active = soup.find('li', class_='bg-blue').text

    cases = []

    cases.append(active.split())
    active = cases[0][1]

    return active


active = active_covid()


# vaccine status

def vaccinations():
    vaccine_stats = []

    vaccine = soup.find('div', class_='col-xs-8 site-stats-count sitetotal').text

    vaccine_stats.append(vaccine.split())
    new = vaccine_stats[0][4]
    new_vaccines = new[1:len(new) - 1]
    current = vaccine_stats[0][3]
    return current, new_vaccines


current, new = vaccinations()


# finding number of deaths
def covid_deaths():
    deaths = []

    death_table = soup.find('li', class_='bg-red').text

    deaths.append(death_table.split())

    new1 = deaths[0][2]
    inc = new1[1:len(new1) - 1]
    change = deaths[0][1]

    return change, inc


currentdeath, newdeath = covid_deaths()


# displaying all cases

def all_cases():
    html_text = requests.get('https://www.mygov.in/covid-19').text
    soup = BeautifulSoup(html_text, 'html.parser')
    block = soup.find('div', class_='iblock t_case')
    count = block.find('span', class_='icount').text
    return count


cases = all_cases()

label_title = tk.Label(root, text="INDIA CORONAVIRUS STATS", font = ('helvetica', 40,'bold'), bg = '#5d8a82', fg = 'white').pack(pady = 40)
# Labels for data
label_activedisplay = tk.Label(root, text="Active Cases: "+str(active), font = ('Helvetica', 20), bg = 'white', fg = 'black', width = '30', borderwidth= 2, relief= 'raised').pack(pady = 15)
# label for vaccine count
label_vaccinedisplay = tk.Label(root, text="Current vaccinations: "+str(current), font = ('Helvetica', 20), bg = 'white', fg = 'black', width = '30', borderwidth= 2, relief= 'raised').pack(pady = 15)
label_newvacdisplay = tk.Label(root, text="New vaccinations: "+str(new), font = ('Helvetica', 20), bg = 'white', fg = 'black', width = '30', borderwidth= 2, relief= 'raised').pack(pady = 15)

# label for deaths
label_curdeath = tk.Label(root, text="Current deaths: "+str(currentdeath), font = ('Helvetica', 20), bg = 'white', fg = 'black', width = '30', borderwidth= 2, relief= 'raised').pack(pady = 15)
label_newdeath = tk.Label(root, text="New deaths: "+str(newdeath), font = ('Helvetica', 20), bg = 'white', fg = 'black', width = '30', borderwidth= 2, relief= 'raised').pack(pady = 15)

# all cases
label_allcases = tk.Label(root, text="Total Cases: "+str(cases), font = ('Helvetica', 25), bg = 'white', fg = 'black', width = '30', borderwidth= 2, relief= 'raised').pack(pady = 15)



root.mainloop()
