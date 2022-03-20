import tkinter as tk


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.main_frame = tk.Frame(self.root)
        self.main_frame.config(background='red', cursor='none')
        self.main_frame.pack(fill=tk.BOTH, expand=tk.TRUE)
        self.root.bind('<F1>', self.opennote)
        self.root.bind('<F2>', self.closenote)
        self.root.bind('<F3>', self.quit)
        l = tk.Label(self.main_frame, text="some text here")
        l.pack()
        self.root.mainloop()

    def opennote(self, event):
        self.n = tk.Text(self.main_frame, background='blue')
        self.n.pack()

    def closenote(self, event):
        self.n.destroy()

    def quit(self, event):
        self.root.destroy()

App()