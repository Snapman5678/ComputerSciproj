from tkinter import *
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



root = Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='#5d8a82')

my_listbox = Listbox(root, width = 55, height = 60, font = ('Times', 18))
my_listbox.pack(pady = 100)
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
