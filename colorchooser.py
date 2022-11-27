from tkinter import *
from tkinter import colorchooser



def click():
    color = colorchooser.askcolor()
    window.config(bg=color[1])


window = Tk()
window.title('ssfsfsfsds')
window.geometry('300x300')
button = Button(text='click me', bg='#29f0aa', foreground='white', command=click)
button.pack()
window.mainloop()
