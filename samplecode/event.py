from tkinter import *
root = Tk()
root.title("Binding Events")
root.geometry("400x100")
def clicked(event):
        label.config(text="Right button clicked")
        print("clicked")
click = Button(root, text="Click Here", font="ariel 15 bold", bg="black", fg="white")
click.pack(padx=30, pady=10)
label = Label(root, text="", font="ariel 15 bold")
label.pack(padx=30, pady=10)
click.bind("<Button-3>", clicked)
root.mainloop()