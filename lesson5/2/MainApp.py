import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd
from CommonUtils import load_txt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.data = None
        self.line = True  # True - линейный график, False - свечной график

        self.figure = plt.Figure(figsize=(6, 6))
        self.plot = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

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
        file_path = filedialog.askopenfilename(initialdir="./aData", title="Выберите файл данных", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.data = load_txt(file_path)

    def visualize_data(self):
        if self.data is not None:
            # fig, ax = plt.subplots()
            # ax.clear()
            self.plot.clear()

            if int(self.graph_type.get()) == 1:
                self.plot.plot(self.data['date'], self.data['close'])
            elif int(self.graph_type.get()) == 2:
                # candlestick_data = list(zip(range(len(self.data)), self.data['open'], self.data['high'], self.data['low'], self.data['close']))
                # self.plot.plot(self.data['date'], candlestick_data)

                prices = pd.DataFrame(self.data,
                                      index=pd.date_range(" 2021-01-01", periods=993, freq=" d "))

                width = .4
                width2 = .05

                # define up and down prices
                up = prices[prices.close >= prices.open]
                down = prices[prices.close < prices.open]

                # define colors to use
                col1 = 'green'
                col2 = 'red'

                # plot up prices
                self.plot.bar(up.index, up.close - up.open, width, bottom=up.open, color=col1)
                self.plot.bar(up.index, up.high - up.close, width2, bottom=up.close, color=col1)
                self.plot.bar(up.index, up.low - up.open, width2, bottom=up.open, color=col1)

                # plot down prices
                self.plot.bar(down.index, down.close - down.open, width, bottom=down.open, color=col2)
                self.plot.bar(down.index, down.high - down.open, width2, bottom=down.open, color=col2)
                self.plot.bar(down.index, down.low - down.close, width2, bottom=down.close, color=col2)

                self.canvas.draw()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()