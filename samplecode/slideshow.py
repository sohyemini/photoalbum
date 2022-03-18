# import required modules
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

# adjust window
root = tk.Tk()
root.geometry("1024x768")
win= Tk()

#Set the geometry of frame
win.geometry("650x250")

# loading the images
org_image = Image.open("./CRW_3550.jpg")
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
print(f"image width:height = {org_image.width} x {org_image.height}")
print(f"screen width:height = {screen_width} x {screen_height}")

#image = org_image.resize((screen_width, screen_height))
image = org_image.resize((1024, 768))
img = ImageTk.PhotoImage(image)
org_image = Image.open("./CRW_3550.jpg")
image = org_image.resize((1024, 768))
img2 = ImageTk.PhotoImage(image)
org_image = Image.open("./CRW_3550.jpg")
image = org_image.resize((1024, 768))
img3 = ImageTk.PhotoImage(image)

'''
사진을 label을 이용해서 출력을 한다.
다음과 같이 라벨의 x, y 위치를 정해서 출력할 수 있다.
'''
l = Label()
l.pack()
l.place(x = 100, y = 100)


label=tk.Label(root, text="파이썬")
label.master.wm_attributes("-transparent", True)
label.config(font=("arial italic", 18), width=10, height=5, fg="black") #, relief="solid"))
label.pack()
label.place(x=500, y=500)


# using recursion to slide to next image
x = 1

# function to change to next image
def move():
    global x
    if x == 4:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    x = x + 1
    root.after(5000, move)


# calling the function
move()

root.mainloop()