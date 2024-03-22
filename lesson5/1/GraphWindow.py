import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GraphWindow(tk.Tk):
    def __init__(self, points):
        super().__init__()
        self.points = points
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()
        
    def onpick(self, event):
        # Обработка события щелчка мыши для выбора точек
        pass
        
    def draw_segment_and_points(self, point_a, point_b):
        # Построение отрезка и разбиение на 20 равных отрезков
        pass