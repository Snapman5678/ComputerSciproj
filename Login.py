import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk,Image
from tkinter import *
import PIL.Image as img


root = tk.Tk()
root.geometry('1200x800')
root.title('COVID-Care')
root.configure(bg = 'white')

def mainnext_front():
    import Frontend

def mainnext_general():
    import Frontend_general

def mainnext_statewise():
    import statewisefinal

def my_profile():
    import Profile


progress = Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate', )

def bar1():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    mainnext_front()

def bar2():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    mainnext_general()

def bar3():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    mainnext_statewise()
def bar4():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    my_profile()

progress.place(relx=0.5, rely=0.98, anchor=CENTER)


button_covid = Button(root,text="India Covid Stats",command=bar1, fg = 'black', height = 5, width = 30, font = ('Helvetica', 25,'bold')).pack(pady = 25)
button_gen = Button(root,text="Top News Headlines",command=bar2,fg = 'black', height = 5, width = 30, font = ('Helvetica', 25, 'bold')).pack(pady = 25)
button_state = Button(root,text="Statewise Covid Data",command=bar3, fg = 'black', height = 5, width = 30, font = ('Helvetica', 25, 'bold')).pack(pady = 25)
button_myprofile = Button(root,text="My Profile",command = bar4, fg = 'black', height = 5, width = 30, font = ('Helvetica', 25, 'bold')).pack(pady = 25)


root.mainloop()
