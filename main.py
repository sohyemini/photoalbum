import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk
from time import sleep

from PhotoFile import Photo

DATA_FILE_NAME  = "photolist.txt"
PHOTO_FILE_PATH = "/Volumes/rickykwak/Photo/Original"
DURATION        = 5

class PhotoFrame(tk.Tk):
    def __init__(self, window=None):
        super().__init__()

        #self.config(cursor='none')

        self.overrideredirect(True)
        if True:
            self.geometry("%dx%d+%d+%d" % (self.winfo_screenwidth()+10, self.winfo_screenheight()+10, -5, -5))
            self.canvas = Canvas(self, width=self.winfo_screenwidth()+10, height=self.winfo_screenheight()+10, bg='black')
        else:
            self.geometry("%dx%d+%d+%d" % (500, 500, 0, 0))
            self.canvas = Canvas(self, width=400, height=400, bg='black')

        self.canvas.pack()

        if os.path.exists(DATA_FILE_NAME):
            os.remove(DATA_FILE_NAME)
        #######
        # 파일 리스트를 만든다.
        self.Photo = Photo(DATA_FILE_NAME, PHOTO_FILE_PATH)
        self.Photo.createFileList()

        self.Run()

    def on_click(self, event):
        print("Exit")

    def Run(self):
        while(1):
            self.displayPhoto()
            sleep(DURATION)


    def displayPhoto(self):
        image, fname, p_date = self.Photo.getRandomPhoto()
        wW = self.winfo_screenwidth()-10
        wH = self.winfo_screenheight() -10

        # 이미지 사이즈는 4:3(1.3)  16:9(1.77)  3:2(1.5) |   3:4(0.75) 9:16(0.56) 2:3(0.67)
        # 화면 사이즈는 1920:1080 (1.78) 1:1
        if image.width/image.height > wW/wH:
            imageH = wH
            imageW = int(image.width * wH / image.height)
        else:
            imageW = wW
            imageH = int(image.height * wW / image.width)

        x = int((wW - imageW) / 2) + 5
        y = int((wH - imageH) / 2) + 5

        pic = image.resize((imageW, imageH))
        picture = ImageTk.PhotoImage(pic)

        w = len(fname)
        pathw = len(PHOTO_FILE_PATH) + 1
        str = fname[pathw:w] + f" ------- [{p_date}]"

        self.canvas.create_image(x, y, anchor=NW, image=picture)
        self.canvas.delete('nameTags')
        self.canvas.create_text(wW/2, wH - 10, text=str, font=("나눔고딕코딩", 14), fill="green", tags=('nameTags',))
        #self.canvas.create_text(wW / 2, 500, text=str, font=("나눔고딕코딩", 14), fill="green", tags=('nameTags',))
        self.canvas.update()


if __name__ == "__main__":
    app = PhotoFrame()
    app.mainloop()