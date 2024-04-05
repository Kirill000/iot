import tkinter as tk
from tkinter import filedialog
from VideoApp import VideoApp
from VideoPlayer import VideoPlayer

class VideoSourceSelection(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Выбор источника видео")

        # Создание переменной для хранения выбранного типа источника
        self.video_source = tk.StringVar()

        # Создание радиокнопок для выбора типа источника
        tk.Radiobutton(self, text="Файл", variable=self.video_source, value="file", command=self.choose_file).pack(anchor=tk.W)
        tk.Radiobutton(self, text="Интернет", variable=self.video_source, value="internet", command=self.choose_file).pack(anchor=tk.W)
        tk.Radiobutton(self, text="Камера", variable=self.video_source, value="camera", command=self.choose_file).pack(anchor=tk.W)

        # Кнопка "Вставить" для выбора файла
        self.btn_insert = tk.Button(self, text="Вставить", command=self.insert_file, state=tk.DISABLED)
        self.btn_insert.pack()

    def choose_file(self):
        self.btn_insert.config(state=tk.NORMAL)
        if self.video_source.get() == "file":
            self.file_path = filedialog.askopenfilename()
            if self.file_path:
                print("Выбранный файл:", self.file_path)
            else:
                print("Файл не выбран")

    def insert_file(self):
        if self.video_source.get() == "file":
            self.destroy()
            VideoApp(video_source=self.file_path).mainloop()
        elif self.video_source.get() == "camera":
            self.destroy()
            VideoApp().mainloop()
           
# Использование класса VideoSourceSelection
app = VideoSourceSelection()
app.mainloop()