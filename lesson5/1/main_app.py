import tkinter as tk
from GraphWindow import GraphWindow
from load_csv_file import load_csv_file
from config import *

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main App")
        self.button_visualize = tk.Button(self, text="Визуализация", command=self.show_graph_window)
        self.button_choose_file = tk.Button(self, text="Выбрать файл", command=self.load_file)
        self.button_visualize.pack()
        self.button_choose_file.pack()
        self.file_path = ""

    def show_graph_window(self):
        if not self.file_path:
            # self.show_error_message("file_not_found")
            pass
        x_coords, z_coords, r_values = load_csv_file(self.file_path)
        graph_window = GraphWindow(self, x_coords, z_coords, r_values)
        graph_window.mainloop()  # Открываем окно для визуализации точек

    def load_file(self):
        self.file_path = tk.filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not self.file_path:
            # self.show_error_message("file_not_found")
            pass
    
    # def show_error_message(self, message_key):
    #     error_message = ERROR_MESSAGES.get(message_key, "An error occurred.")
    #     error_window = ErrorWindow(error_message)
    #     error_window.mainloop()