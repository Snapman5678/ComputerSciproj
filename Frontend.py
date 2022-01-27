from tkinter import *
from tkinter.ttk import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("COVID-care")
root.geometry('600x700')
root.configure(background='#5d8a82')

# entry for state name
label_state = Label(root, text="Enter State").place(relx=0.4, rely=0.1, anchor=CENTER)
input_state = Entry(root, width=30).place(relx=0.6, rely=0.1, anchor=CENTER)

html_text = requests.get('https://www.mohfw.gov.in/').text
soup = BeautifulSoup(html_text, 'lxml')


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
    soup = BeautifulSoup(html_text, 'lxml')
    block = soup.find('div', class_='iblock t_case')
    count = block.find('span', class_='icount').text
    return count


cases = all_cases()


# statewise data

def statewise():
    s1 = []
    state_final = []
    html_text = requests.get('https://prsindia.org/covid-19/cases').text
    soup = BeautifulSoup(html_text, 'lxml')
    table = soup.find('table', class_='table table-striped table-bordered')
    body = table.find('tbody')
    state_names = body.find_all('td')
    for i in state_names:
        a = i.text
        s1.append(a)
    i = 0
    state = []
    for j in s1:
        if i < 6:
            state.append(j)
            i = i + 1
        elif i == 6:
            state_final.append(state)
            state = []
            state.append(j)
            i = 0

    name = input_state
    for i in range(len(state_final)):
        if state_final[i][1] == name:
            sconfirmed = state_final[i][2]
            sactive = state_final[i][3]
            scured = state_final[i][4]
            sdeaths = state_final[i][5]
    return sconfirmed, sactive, scured, sdeaths


state_confirmed, state_active, state_cured, state_deaths = statewise()

# Labels for data
label_activedisplay = Label(root, text="Active Cases").place(relx=0.4, rely=0.2, anchor=CENTER)
label_active = Label(root, text=active).place(relx=0.6, rely=0.2, anchor=CENTER)

# label for vaccine count
label_vaccinedisplay = Label(root, text="Current vaccinations").place(relx=0.2, rely=0.3, anchor=CENTER)
label_vaccine = Label(root, text=current).place(relx=0.4, rely=0.3, anchor=CENTER)
label_newvacdisplay = Label(root, text="New vaccinations").place(relx=0.6, rely=0.3, anchor=CENTER)
lebel_newvac = Label(root, text=new).place(relx=0.8, rely=0.3, anchor=CENTER)

# label for deaths
label_curdeath = Label(root, text="Current deaths").place(relx=0.2, rely=0.4, anchor=CENTER)
label_deaths = Label(root, text=currentdeath).place(relx=0.4, rely=0.4, anchor=CENTER)
label_newdeath = Label(root, text="New deaths").place(relx=0.6, rely=0.4, anchor=CENTER)
label_ndeath = Label(root, text=newdeath).place(relx=0.8, rely=0.4, anchor=CENTER)

# all cases
label_allcases = Label(root, text="Cases").place(relx=0.4, rely=0.5, anchor=CENTER)
label_state = Label(root, text=cases).place(relx=0.6, rely=0.5, anchor=CENTER)

# state
label_statetitle = Label(root, text="State information").place(relx=0.5, rely=0.6, anchor=CENTER)
label_sconfirm = Label(root, text="Confirmed Cases").place(relx=0.2, rely=0.7, anchor=CENTER)
label_sconfirmdis = Label(root, text=state_confirmed).place(relx=0.4, rely=0.7, anchor=CENTER)
label_sactive = Label(root, text="Active Cases").place(relx=0.6, rely=0.7, anchor=CENTER)
label_sactivedisplay = Label(root, text=state_active).place(relx=0.8, rely=0.7, anchor=CENTER)
label_scured = Label(root, text="Cured Cases").place(relx=0.2, rely=0.8, anchor=CENTER)
label_scureddisplay = Label(root, text=state_cured).place(relx=0.4, rely=0.8, anchor=CENTER)
label_sdeaths = Label(root, text="Deaths").place(relx=0.6, rely=0.8, anchor=CENTER)
label_sdeathdis = Label(root, text=state_deaths).place(relx=0.8, rely=0.8, anchor=CENTER)

root.mainloop()