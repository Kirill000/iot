import tkinter as tk
from mainWindow import MainWindow
from pathlib import Path

if __name__ == "__main__":
    root = tk.Tk()
    
    path = Path(__file__).resolve().parent
    icon_file = path.joinpath("interest.ico")
    root.iconbitmap(icon_file)
    
    root.title("Integerst")
    
    window = MainWindow(root)
    
    root.bind("<Escape>", window.quit)
    
    root.mainloop()