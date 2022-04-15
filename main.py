from tkinter import Tk, Entry, END, Button
from nationalStats import *
import requests
import news
import stateStats


def tableMaker(root, data: list, widths):
    for i in range(len(data)):
        for j in range(len(data[0])):
            e = Entry(root, width=widths[j])
            e.grid(row=i, column=j)
            e.insert(END, data[i][j])


def showStateWise():
    window = Tk()
    tableMaker(window, data=stateStats.stateWise(), widths=(2, 40, 8, 8, 8, 8))
    window.mainloop()


def showNews():
    window = Tk()
    head = news.news()
    tableMaker(window, [[a] for a in head], widths=(len(max(head)),))
    window.mainloop()


def showNationalStats():
    window = Tk()
    html_text = requests.get('https://www.mohfw.gov.in/').text
    knorr = BeautifulSoup(html_text, 'html.parser')
    stats = [*all_cases(), *covid_deaths(soup=knorr), *active_covid(soup=knorr), *vaccinations(soup=knorr)]
    stats = [stats[i * 2: (i + 1) * 2] for i in range((len(stats) + 1) // 2)]
    tableMaker(window, data=stats, widths=(20, 20))
    window.mainloop()


if __name__ == '__main__':
    mainWindow = Tk()
    font = ('Helvetica', 25, 'bold')
    Button(mainWindow, text='India Covid Stats', command=showNationalStats, height=5, width=30, font=font).pack()
    Button(mainWindow, text='News', command=showNews, height=5, width=30, font=font).pack()
    Button(mainWindow, text='State Wise Covid Stats', command=showStateWise, height=5, width=30, font=font).pack()
    mainWindow.mainloop()
