from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://timesofindia.indiatimes.com/world').text
soup = BeautifulSoup(html_text, 'html.parser')
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

#need you to do you thing here
def output():
    with open("news.text",'r') as f:
        list = f.readlines()
        text = list[-1]
        return text

news=output()

root = Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='#5d8a82')



label= Label(root,text="news",width=600).place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()