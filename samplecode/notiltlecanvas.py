import tkinter as tk
from tkinter import *
from PhotoFile import Photo
from PIL import ImageTk
DATA_FILE_NAME  = "../photolist.txt"
PHOTO_FILE_PATH = "/Volumes/Photo/Original"
DURATION        = 6

class FloatingWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.center()
        photo = Photo(DATA_FILE_NAME, PHOTO_FILE_PATH)
        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack()

        image = photo.getRandomPhoto()
        pic = image.resize((1024, 768))
        picture = ImageTk.PhotoImage(pic)
        self.canvas.create_image(0, 0, anchor=NW, image=picture)
        self.canvas.place(x=0, y=0, height=image.height, width=image.width)

    def center(self):
        width = 300
        height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width / 2)
        y_coordinate = (screen_height / 2) - (height / 2)

        self.geometry("%dx%d+%d+%d" % (width, height,
                                       x_coordinate, y_coordinate))

if __name__ == "__main__":
    app = FloatingWindow()
    app.mainloop()