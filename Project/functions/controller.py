import tkinter as tk
import time

class App(tk.Frame):

    root = tk.Tk()

    def __init__(self, parent = root):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title('SDC')
        self.parent.geometry('500x500')


myapp = App()
myapp.mainloop()