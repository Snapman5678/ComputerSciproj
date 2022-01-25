from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

root = Tk()
root.geometry('600x700')
root.title('COVID-Care')
root.configure(background='#5d8a82')


def mainnext():
    root.destroy()
    import Login


canvas = Canvas(root, width=300, height=300)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
logo = Image.open("COVID-Care-logos.jpeg")
logoresize = logo.resize((300, 300))
logofin = ImageTk.PhotoImage(logoresize)
canvas.create_image(150, 150, image=logofin)

progress = Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate', )



def bar():
    import time
    progress['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 50
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progress['value'] = 80
    root.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    mainnext()


progress.place(relx=0.5, rely=0.98, anchor=CENTER)
Button(root, text = 'For your health click here', command = bar).place(relx=0.5, rely=0.1, anchor=CENTER)

root.mainloop()
