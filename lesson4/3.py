from tkinter import *

window = Tk()
window.title("IOT")
window.geometry('550x400')
window.configure(bg='orange')

def clicked():
    lbl.configure(text='Button is clicked!', foreground='white', font='bold', background='blue')

window.columnconfigure(index=[0, 1], weight=1)
window.rowconfigure(index=[0, 1], weight=1)

btn = Button(window, text="Click", background='white', foreground='blue', borderwidth=2, relief="solid", command=clicked)
lbl = Label(window, text="", background='orange')

btn.pack(padx=10, pady=10, ipadx=10, ipady=10)
lbl.pack(padx=10, pady=10, ipadx=10, ipady=10)

window.mainloop()