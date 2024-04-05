import cv2
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

class VideoApp(tk.Tk):
    def __init__(self, video_source=0):
        super().__init__()
        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)
        
        self.canvas = tk.Canvas(self)
        self.canvas.place(x=0, y=0)
        
        self.delay = 10
        self.photo = None
        self.playing = False
        
        self.btn_play_pause = tk.Button(self, text="Запуск", command=self.play_pause)
        self.btn_play_pause.place(x=10, y=10)
        
        self.btn_snapshot = tk.Button(self, text="Снимок", command=self.take_photo)
        self.btn_snapshot.place(x=10, y=40)
        
        self.btn_settings = tk.Button(self, text="Настройки", command=self.open_settings)
        self.btn_settings.place(x=10, y=70)
        
        self.thread = None
        self.lock = threading.Lock()
        self.event = threading.Event()
        self.cycleResult = True
        
        self.update()

    def update(self):
        ret, frame = self.vid.read()
        
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(image=frame)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        if self.playing:
            self.after(self.delay, self.update)
    
    def play_pause(self):
        if self.playing:
            self.playing = False
            self.btn_play_pause.config(text="Запуск")
        else:
            self.playing = True
            self.btn_play_pause.config(text="Пауза")
            self.update()
    
    def take_photo(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite("snapshot.jpg", frame)
            
        if self.thread:
            self.event.set()
            self.thread.join()
            self.thread = None
        else:
            if not self.event.is_set():
                self.thread = threading.Thread(target=self.find_in_stream, args=(self.cycleResult, self.lock, self.event))
                self.thread.start()
    
    def find_in_stream(self, cycle_result, lock, event):
        self.canvas_snap = tk.Canvas(self, width=200, height=150)
        self.canvas_snap.place(x=400, y=10)
        
        while cycle_result and not event.is_set():
            with lock:
                ret, frame = self.vid.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.flip(frame, 1)  # horizontal flip
                    frame = Image.fromarray(frame)
                    photo_snap = ImageTk.PhotoImage(image=frame)
                    self.canvas_snap.create_image(0, 0, image=photo_snap, anchor=tk.NW)
    
    def save_photo(self):
        ret, frame = self.vid.read()
        if ret:
            cv2.imwrite("snapshot_save.jpg", frame)
    
    def open_settings(self):
        print("Settings opened")  # Placeholder for the actual settings functionality
    
    def close(self):
        self.event.set()
        if self.vid.isOpened():
            self.vid.release()
        self.destroy()

# Использование класса VideoApp для отображения видео с камеры
app = VideoApp()
app.mainloop()