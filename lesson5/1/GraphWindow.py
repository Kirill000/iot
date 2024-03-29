import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from DiagramWindow import DiagramWindow
from scipy.interpolate import LinearNDInterpolator
from scipy.spatial import Delaunay

class GraphWindow(tk.Toplevel):
    def __init__(self, master, x_coords, z_coords, r_values):
        super().__init__(master)
        self.n_points = x_coords.pop(len(x_coords)-1).split("/")
        self.x_coords = [int(x) for x in x_coords]
        self.z_coords = [int(x) for x in z_coords]
        self.r_values = [int(x) for x in r_values]
        self.title("Graph Window")
        self.geometry("800x600")
        self.plot_points = []
        self.selected_points = []

        self.figure = Figure(figsize=(6, 6))
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack()

        self.plot.scatter(self.x_coords, self.z_coords, c=self.r_values, cmap='coolwarm', label='R values')
        self.canvas.draw()

        self.canvas.mpl_connect('button_press_event', self.on_click)

        self.button_build_epure = tk.Button(self, text="Построение эпюры", command=self.build_epure)
        self.button_build_epure.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    def calculate_r_values(self, x_values, n_points):
        x1, z1 = self.selected_points[0]
        x2, z2 = self.selected_points[1]

        n_points = np.array([[x1, z1], [x2, z2], [x1, z1 + 1e-6], [x2, z2 + 1e-6]])
        tri = Delaunay(n_points)
        
        interp = LinearNDInterpolator(tri, [self.r_values[0], self.r_values[1], 0, 0])
        x_coordinates_new = np.linspace(x1, x2, len(self.n_points))
        z_coordinates_new = [_ for _ in self.n_points]

        # z_new = linear_interpolation(points, self.r_values, x_values)
        print(x_coordinates_new, z_coordinates_new)
        return x_coordinates_new, z_coordinates_new

    def build_epure(self):
        n_points = 100
        x_new, r_new = self.calculate_r_values([self.x_coords[0], self.x_coords[1]], n_points)
        self.diagram_window = DiagramWindow(self, x_new, r_new)
        
    def on_click(self, event):
        if len(self.selected_points) < 2:
            x, z = event.xdata, event.ydata
            self.plot_points.append((x, z))
            self.plot.plot(x, z, marker='o', color='black')

            if len(self.selected_points) == 1:
                x1, z1 = self.selected_points[0]
                x2, z2 = (x, z)
                n_points = 18

                for i in range(1, n_points + 1):
                    ratio = i / (n_points + 1)
                    n_x = x1 + ratio * (x2 - x1)
                    n_z = z1 + ratio * (z2 - z1)
                    self.plot_points.append((n_x, n_z))
                    self.plot.plot(n_x, n_z, marker='.', color='black')

            self.selected_points.append((x, z))
            self.canvas.draw()