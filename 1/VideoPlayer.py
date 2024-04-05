import cv2
import tkinter as tk
from PIL import Image, ImageTk
from appSettings import *

class VideoPlayer(tk.Tk):
    def __init__(self, video_file, width=100, height=100):
        super().__init__()
        self.cap = cv2.VideoCapture(filename=r"C:\Users\Lenovo\Desktop\iot\lesson6\1\vData\cats_video.mp4")
        self.button = tk.Button(self, text='stop', command=self.pause_unpause)
        self.button.place(x=0, y=0)
        self.canvas = tk.Canvas(self, height=height, width=width)
        self.delay = int(1000 / self.cap.get(cv2.CAP_PROP_FPS))
        self.update()
        
    def place(self, x, y):
        self.canvas.place(x=x, y=y)
        self.update()

    def update(self):
        if self.button['text'] == 'stop':
            ret, frame = self.cap.read()
        else:
            self.after(self.delay, self.update)
            return
        if ret:
            if self.button['text'] == 'stop':
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
            self.after(self.delay, self.update)
        else:
            self.cap.release()
    
    def pause_unpause(self):
        if self.button['text'] == 'stop':
            self.button['text'] = 'play'
        else:
            self.button['text'] = 'stop'
VideoPlayer(0).mainloop()

# def run_video(file):
    
#     def pause_unpause():
#         if button['text'] == 'stop':
#             button['text'] = 'play'
#         else:
#             button['text'] = 'stop'

#     window = tk.Tk()
#     window.geometry('1000x1000')
#     button = tk.Button(window, text='stop', command=pause_unpause)
#     button.place(x=0, y=0)
#     # print(file)
#     video = VideoPlayer(file, master=window, button=button, width=800, height=1000)
#     video.place(x=50, y=0)


#     window.mainloop()
# run_video(0)