import tkinter as tk
from appSettings import WIDTH, HEIGHT, MARGIN
from Pong import Pong

if __name__ == "__main__":
    root = tk.Tk()
    pong = Pong(root, WIDTH, HEIGHT, MARGIN)
    
    root.bind("<KeyPress>", pong.keypress)
    root.bind("<KeyRelease>", pong.keyrelease)
    root.wm_protocol("WM_DELETE_WINDOW", pong.kill_timer)
    
    root.mainloop()