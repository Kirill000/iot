import tkinter as tk
from tkinter import messagebox

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

        self.principalScale = tk.Scale(self, from_=0, to=10000, resolution=100, orient=tk.HORIZONTAL, variable=self.principal)
        self.principalScale.grid(row=0, column=1)

        rateLabel = tk.Label(self, text="Rate (%):")
        rateLabel.grid(row=1, column=0, sticky=tk.W, padx=10)

        self.rateScale = tk.Scale(self, from_=0, to=20, resolution=1, orient=tk.HORIZONTAL, variable=self.rate)
        self.rateScale.grid(row=1, column=1)

        yearsLabel = tk.Label(self, text="Years:")
        yearsLabel.grid(row=2, column=0, sticky=tk.W, padx=10)

        self.yearsScale = tk.Scale(self, from_=0, to=50, resolution=1, orient=tk.HORIZONTAL, variable=self.years)
        self.yearsScale.grid(row=2, column=1)

        amountLabel = tk.Label(self, text="Amount:")
        amountLabel.grid(row=3, column=0, sticky=tk.W, padx=10)

        self.actualAmountLabel = tk.Label(self, textvariable=self.amount, relief=tk.SUNKEN, anchor=tk.E)
        self.actualAmountLabel.grid(row=3, column=1)

        self.btn = tk.Button(self, text="Calc", command=self.update_ui)
        self.btn.grid(row=4, column=1)

        # self.update_ui()

        self.parent.bind("<Escape>", self.quit)

        self.context_menu = tk.Menu(self.parent, tearoff=0)
        self.context_menu.add_command(label="Increase Years", command=self.increase_years)
        self.context_menu.add_command(label="Decrease Years", command=self.decrease_years)
        self.context_menu.add_command(label="Exit", command=self.exit)

    def exit(self):
        self.master.quit()

    def update_ui(self, *ignore):
        p = self.principal.get()
        r = self.rate.get()
        y = self.years.get()

        amount = p * (1 + r / 100) ** y
        self.amount.set(f"{amount:.2f}")
        self.show_message()

    def quit(self, event=None):
        self.parent.destroy()

    def increase_years(self):
        self.years.set(self.years.get() + 1)
        self.update_ui()

    def decrease_years(self):
        self.years.set(self.years.get() - 1)
        self.update_ui()

    def show_message(self):
        messagebox.showinfo("Success", "Amount calculated successfully!")

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)