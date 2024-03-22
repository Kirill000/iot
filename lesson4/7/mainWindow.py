import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, parent):
        super(MainWindow, self).__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)
        
        self.principal = tk.DoubleVar()
        self.rate = tk.DoubleVar()
        self.years = tk.IntVar()
        self.amount = tk.StringVar()
        
        principalLabel = tk.Label(self, text="Principal:")
        principalLabel.grid(row=0, column=0, sticky=tk.W, padx=10)
        
        self.principalScale = tk.Scale(self, from_=0, to=10000, resolution=100, orient=tk.HORIZONTAL, variable=self.principal, command=self.updateUi)
        self.principalScale.grid(row=0, column=1)
        
        rateLabel = tk.Label(self, text="Rate (%):")
        rateLabel.grid(row=1, column=0, sticky=tk.W, padx=10)
        
        self.rateScale = tk.Scale(self, from_=0, to=20, resolution=1, orient=tk.HORIZONTAL, variable=self.rate, command=self.updateUi)
        self.rateScale.grid(row=1, column=1)
        
        yearsLabel = tk.Label(self, text="Years:")
        yearsLabel.grid(row=2, column=0, sticky=tk.W, padx=10)
        
        self.yearsScale = tk.Scale(self, from_=0, to=50, resolution=1, orient=tk.HORIZONTAL, variable=self.years, command=self.updateUi)
        self.yearsScale.grid(row=2, column=1)
        
        amountLabel = tk.Label(self, text="Amount:")
        amountLabel.grid(row=3, column=0, sticky=tk.W, padx=10)
        
        self.actualAmountLabel = tk.Label(self, textvariable=self.amount, relief=tk.SUNKEN, anchor=tk.E)
        self.actualAmountLabel.grid(row=3, column=1)
        
        self.updateUi()
        
        self.parent.bind("<Escape>", self.quit)
    
    def updateUi(self, *ignore):
        p = self.principal.get()
        r = self.rate.get()
        y = self.years.get()
        
        amount = p * (1 + r/100) ** y
        self.amount.set(f"{amount:.2f}")
        
    def quit(self, event=None):
        self.parent.destroy()