import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.data = None
        self.line = True  # True - линейный график, False - свечной график

        self.button_load = tk.Button(self, text="Загрузить данные", command=self.load_data)
        self.button_load.place(relx=0.1, rely=0.01)

        self.button_visualize = tk.Button(self, text="Отобразить", command=self.visualize_data)
        self.button_visualize.place(relx=0.1, rely=0.05)

        self.graph_type = tk.IntVar()
        self.radio_line = tk.Radiobutton(self, text="Линейный график", variable=self.graph_type, value=1)
        self.radio_line.place(relx=0.1, rely=0.1)

        self.radio_candle = tk.Radiobutton(self, text="Свечевой график", variable=self.graph_type, value=2)
        self.radio_candle.place(relx=0.1, rely=0.15)

    def load_data(self):
        file_path = filedialog.askopenfilename(initialdir="./aData", title="Выберите файл данных", filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)

    def visualize_data(self):
        if self.data is not None:
            fig, ax = plt.subplots()
            ax.clear()

            if self.line:
                ax.plot(self.data['Дата'], self.data['Цена закрытия'])
            else:
                candlestick_data = list(zip(range(len(self.data)), self.data['Цена открытия'], self.data['Самая высокая цена'], self.data['Самая низкая цена'], self.data['Цена закрытия']))
                ax.plot(self.data['Дата'], candlestick_data)

            plt.show()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()