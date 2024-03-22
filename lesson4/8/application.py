import tkinter as tk
from mainWindow import MainWindow
from pathlib import Path

if __name__ == "__main__":
    root = tk.Tk()

    def quit(event=None) -> None:
        root.destroy()

    mainmenu = tk.Menu(root)
    root.config(menu=mainmenu)

    filemenu = tk.Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Выход", command=quit)

    helpmenu = tk.Menu(mainmenu, tearoff=0)

    helpmenu2 = tk.Menu(helpmenu, tearoff=0)
    helpmenu2.add_command(label="Локальная справка")
    helpmenu2.add_command(label="На сайте")

    helpmenu.add_cascade(label="Помощь", menu=helpmenu2)
    helpmenu.add_command(label="О программе")

    mainmenu.add_cascade(label="Файл", menu=filemenu)
    
    path = Path(__file__).resolve().parent
    icon_file = path.joinpath("interest.ico")
    root.iconbitmap(icon_file)
    
    root.title("Integerst")
    
    window = MainWindow(root)
    
    root.bind("<Escape>", window.quit)
    
    root.mainloop()