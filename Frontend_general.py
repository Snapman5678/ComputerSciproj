import tkinter as tk
from tkinter.ttk import *
import requests
from bs4 import BeautifulSoup
import webbrowser


html_text = requests.get('https://timesofindia.indiatimes.com/world').text
soup = BeautifulSoup(html_text, 'html.parser')
head = soup.find('div', class_ = 'top-newslist')

titles = []

for title in head.find_all('a'):
    headline = title.get('title')
    titles.append(headline)



root = tk.Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='black')

label_title = tk.Label(root, text="TOP WORLD HEADLINES", font = ('helvetica', 40,'bold'), bg = 'black', fg = 'white').pack(pady = 15)

my_listbox = tk.Listbox(root, width = 55, height = 60, font = ('Times', 20), bg = 'aqua', fg = 'black', justify= 'center')
my_listbox.pack(pady = 40,fill = 'both', expand = 1)
i = 0
j = 1
for news in titles[1::]:
    if i < 3*len(titles) - 1:
        my_listbox.insert(i, news)
        i = i + 1
        my_listbox.insert(i, '\n\n\n\n')
        i = i + 1

root.mainloop()

print(titles)
