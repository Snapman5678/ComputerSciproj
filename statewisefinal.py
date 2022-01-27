
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("COVID-care")
root.geometry('600x700')
root.configure(background='#5d8a82')


# statewise data

def statewise():
    s1 = []
    state_final = [['0','STATE','TOTAL CASES', 'ACTIVE','CURED','DEATHS']]
    html_text = requests.get('https://prsindia.org/covid-19/cases').text
    soup = BeautifulSoup(html_text, 'html.parser')
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
            i = 1

    return state_final

# state
my_tree = ttk.Treeview(root)
my_tree.pack(expand = 1, fill= 'both')

style = ttk.Style()
style.configure('Treeview', rowheight = 20)
my_tree['columns'] = ('STATE', 'TOTAL CASES', 'ACTIVE CASES', 'CURED','DEATHS')

my_tree.column('#0', width = 0, stretch = NO)
my_tree.column('STATE', width = 120)
my_tree.column('TOTAL CASES', width = 120)
my_tree.column('ACTIVE CASES', width = 110)
my_tree.column('CURED', width = 100)
my_tree.column('DEATHS', width = 100)

my_tree.heading('#0', text = '', anchor = W)
my_tree.heading('STATE', text = 'STATE', anchor = W)
my_tree.heading('TOTAL CASES', text = 'TOTAL CASES', anchor = W)
my_tree.heading('ACTIVE CASES', text = 'ACTIVE CASES', anchor = W)
my_tree.heading('CURED', text = 'CURED', anchor = W)
my_tree.heading('DEATHS', text = 'DEATHS', anchor = W)

#inserting
final = statewise()
count = 0
for data in final:
    my_tree.insert(parent = '', index = 'end', iid = count, text= '', values = (data[1], data[2], data[3], data[4], data[5]))
    count = count + 1

root.mainloop()
