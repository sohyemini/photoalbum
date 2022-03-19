import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk
from time import sleep

from PhotoFile import Photo

DATA_FILE_NAME  = "photolist.txt"
PHOTO_FILE_PATH = "/home/pi/media/Photo/Original"
DURATION        = 120

class PhotoFrame(tk.Tk):
    def __init__(self, window=None):
        super().__init__()

        self.overrideredirect(True)
        if False:
            self.geometry("%dx%d+%d+%d" % (self.winfo_screenwidth()+10, self.winfo_screenheight()+10, -5, -5))
            self.canvas = Canvas(self, width=self.winfo_screenwidth()+10, height=self.winfo_screenheight()+10, bg='black')
        else:
            self.geometry("%dx%d+%d+%d" % (500, 500, 0, 0))
            self.canvas = Canvas(self, width=400, height=400, bg='black')

        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.pack()

        #if os.path.exists(DATA_FILE_NAME):
        #    os.remove(DATA_FILE_NAME)
        #######
        # 파일 리스트를 만든다.
        self.Photo = Photo(DATA_FILE_NAME, PHOTO_FILE_PATH)
        #self.Photo.createFileList()

        self.Run()

    def on_click(self, event):
        print("Exit")

    def Run(self):
        while(1):
            self.displayPhoto()
            sleep(DURATION)


    def displayPhoto(self):
        image, fname, p_date = self.Photo.getRandomPhoto()
        wW = self.winfo_screenwidth()
        wH = self.winfo_screenheight()

        #if image.height/image.width > wH/wW :   # 가로기준 리사이즈
        #    imageH = wH
        #    imageW = int(image.width * wH / image.height)
        #else:                                   # 세로기준 리사이즈
        # 가로기준 리사이즈는 사진이 좁아보인다. 아무래도 넓게 보이는 것이 좋아서 이렇게 하기로 함
        imageW = wW
        imageH = int(image.height * wW / image.width)

        x = int((wW - imageW) / 2)
        y = int((wH - imageH) / 2)

        pic = image.resize((imageW, imageH))
        picture = ImageTk.PhotoImage(pic)

        w = len(fname)
        pathw = len(PHOTO_FILE_PATH) + 1
        str = fname[pathw:w] + f" ------- [{p_date}]"

        self.canvas.create_image(x, y, anchor=NW, image=picture)
        self.canvas.delete('nameTags')
        self.canvas.create_text(wW/2, wH - 10, text=str, font=("나눔고딕코딩", 10), fill="white", tags=('nameTags',))
        self.canvas.update()


if __name__ == "__main__":
    app = PhotoFrame()
    #app.config(cursor="None")
    app.mainloop()