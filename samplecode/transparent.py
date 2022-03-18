from tkinter import *
from PIL import ImageTk
from PIL import Image
tk = Tk()
canvas = Canvas(tk, width = 1024, height = 768)
canvas.pack()
org_image = Image.open("../CRW_3550.jpg")

image = org_image.resize((1024, 768))
testImage = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor = NW, image = testImage)
canvas.create_text(150, 100, text = "테스트 문자열 입니다.",
                   font = ("나눔고딕코딩", 20), fill = "blue")


tk.mainloop()