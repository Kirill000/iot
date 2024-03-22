import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
from pathlib import Path
import glob

class PhotoViewer:
    def __init__(self, root, image_folder):
        self.root = root
        self.root.title("Photo Viewer")
        self.root.columnconfigure(index=[0, 1, 2], weight=1)
        self.root.rowconfigure(index=[0, 1, 2], weight=1)

        
        self.image_folder = Path(image_folder)
        self.image_list = list(path.glob("images/*.png"))
        self.total_images = len(self.image_list)
        self.current_image = 0
        print(self.image_list)

        img = Image.open(self.image_list[self.current_image])
        x, y = img.size

        if x >= 300 or y >= 300:
            img = img.resize((x//2, y//2))
        self.photo_image = ImageTk.PhotoImage(img)

        self.image_label = Label(root, image=self.photo_image)
        self.image_label.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10, padx=10, pady=10)
        
        self.status_label = Label(root, text=f"Image {self.current_image + 1}/{self.total_images}", bd=1, relief="sunken", anchor="e")
        self.status_label.grid(row=1, column=0, columnspan=3, sticky="we")
        
        self.button_back = Button(root, text="Previous", command=self.back, state="disabled")
        self.button_back.grid(row=2, column=0)
        
        self.button_quit = Button(root, text="Quit", command=root.quit)
        self.button_quit.grid(row=2, column=1)
        
        self.button_forward = Button(root, text="Next", command=lambda: self.forward(1))
        self.button_forward.grid(row=2, column=2)
        
    def back(self):
        self.current_image -= 1
        self.show_image()
        
    def forward(self, steps):
        self.current_image += steps
        self.show_image()
    
    def show_image(self):
        if self.current_image < 0:
            self.current_image = 0
        elif self.current_image >= self.total_images:
            self.current_image = self.total_images - 1

        img = Image.open(self.image_list[self.current_image])

        x, y = img.size
        if x >= 300 or y >= 300:
            img = img.resize((x//2, y//2))
        
        self.photo_image = ImageTk.PhotoImage(img)
        self.image_label.grid_forget()
        self.image_label = Label(self.root, image=self.photo_image)
        self.image_label.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10, padx=10, pady=10)
        
        self.status_label.config(text=f"Image {self.current_image + 1}/{self.total_images}")
        
        if self.current_image == 0:
            self.button_back.config(state="disabled")
        else:
            self.button_back.config(state="normal")
        
        if self.current_image == self.total_images - 1:
            self.button_forward.config(state="disabled")
        else:
            self.button_forward.config(state="normal")
        

if __name__ == "__main__":
    root = tk.Tk()

    path = Path(__file__).resolve().parent
    icon_file = path.joinpath("test_axe.ico")
    root.iconbitmap(icon_file)
    
    photo_viewer = PhotoViewer(root, "images")
    
    root.mainloop()