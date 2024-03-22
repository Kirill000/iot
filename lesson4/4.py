from tkinter import *

window = Tk()
window.title("IOT")
window.geometry('550x400')
window.configure(bg='orange')

class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='white', *args, **kwargs):
        
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

def clicked():
    etr.get()
    lbl.configure(text="Hi, "+etr.get(), foreground='white', font='bold', background='blue', width=50)

window.columnconfigure(index=0, weight=1)

window.columnconfigure(index=[0, 1], weight=1)
window.rowconfigure(index=[0, 1], weight=1)

etr = EntryWithPlaceholder(window, "Enter your name:", background='blue', foreground='white', borderwidth=5, relief="solid")
btn = Button(window, text="Click", background='white', foreground='blue', borderwidth=2, relief="solid", command=clicked)
lbl = Label(window, text="", background='orange')

etr.pack(padx=10, pady=10, ipadx=10, ipady=10)
btn.pack(padx=10, pady=10, ipadx=10, ipady=10)
lbl.pack(padx=10, pady=10, ipadx=10, ipady=10)

window.mainloop()