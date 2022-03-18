import tkinter as tk


class FloatingWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)
        self.center()

        self.label = tk.Label(self, text="Grab one of the blue")
        self.label.pack(side="top", fill="both", expand=True)

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