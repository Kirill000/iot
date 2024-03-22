import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DiagramWindow(tk.Tk):
    def __init__(self, interpolated_points):
        super().__init__()
        self.interpolated_points = interpolated_points
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()
        
    def draw_diagram(self):
        # Построение графика с значениями R по прямой AB
        pass