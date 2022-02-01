from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

root = Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='#5d8a82')

def mainnext_front():
    root.destroy()
    import Frontend

def mainnext_general():
    root.destroy()
    import Frontend_general

def mainnext_statewise():
    root.destroy()
    import statewisefinal


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

progress.place(relx=0.5, rely=0.98, anchor=CENTER)

button_covid = Button(root,text="Covid News",command=bar1).place(relx=0.5,rely=0.3,anchor=CENTER)
button_gen = Button(root,text="General News",command=bar2).place(relx=0.5,rely=0.5,anchor=CENTER)
button_state = Button(root,text="Statewise News",command=bar3).place(relx=0.5,rely=0.7,anchor=CENTER)


root.mainloop()

