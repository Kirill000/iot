from tkinter import *

window = Tk()
window.title("IOT")
window.geometry('550x400')
window.configure(bg='orange')

window.columnconfigure(index=[0, 1], weight=1)
window.rowconfigure(index=[0, 1], weight=1)

lbl = Label(window, text="Hello World!", foreground='white', font='bold', background='blue', height=1000, width=20000)
lbl2 = Label(window, text="My name is Kirill Tandalov", foreground='white', font='bold', background='blue', width=20000, height=10000)  
lbl3 = Label(window, text="", foreground='white', font='bold', background='blue', width=200000, height=10000)  
lbl4 = Label(window, text="", foreground='white', font='bold', background='blue', width=200000, height=10000)  
lbl.grid(column=0, row=0, ipadx=10, ipady=10, padx=10, pady=10)
lbl2.grid(column=1, row=1, ipadx=10, ipady=10, padx=10, pady=10)
lbl3.grid(column=1, row=0, ipadx=10, ipady=10, padx=10, pady=10)
lbl4.grid(column=0, row=1, ipadx=10, ipady=10, padx=10, pady=10)
window.mainloop()