from tkinter import *

window = Tk()
window.title("IOT")
window.geometry('400x250')
window.configure(bg='orange')
lbl = Label(window, text="Hello World!", foreground='white', font='bold', background='blue')  
lbl.pack(padx=10, pady=100, ipadx=10, ipady=10)
window.mainloop()