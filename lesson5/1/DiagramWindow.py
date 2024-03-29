import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DiagramWindow(tk.Toplevel):
    def __init__(self, master, x_values, r_values):
        super().__init__(master)
        self.title("Diagram Window")
        self.geometry("800x600")
        self.figure = plt.Figure(figsize=(6, 6))
        self.plot = self.figure.add_subplot(111)
        r_values = list(map(float, r_values))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # Добавляем с полным заполнением
        self.plot.plot(x_values, r_values, color='red', label='Interpolated R values')
        self.plot.set_xlabel('X')
        self.plot.set_ylabel('R')
        self.plot.legend()
        self.canvas.draw()