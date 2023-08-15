import tkinter as tk
from tkinter import ttk
import tkinter.font as font

class App(tk.Tk):
    #creacion de la ventana
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #configuracion de la ventana
        self.configure(bg='black')
        self.title('SDC - S1')
        self.columnconfigure(0 , weight = 1)
        self.rowconfigure(0, weight = 1)

        #creacion del contenedor maestro
        main = tk.Frame(self, bg = 'red')
        main.grid(padx = 40, pady = 50, sticky = 'nsew')

        #creacion del diccionario de pantallas
        self.all_frames = dict()

        #llenado del diccionario de pantallas
        for F in (login1, Frame2):
            frame = F(main, self)

            self.all_frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(login1)

    def show_frame(self, called_Frame):
        frame = self.all_frames[called_Frame]

        frame.tkraise()

class login1(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = 'red')

        self.username = tk.StringVar()
        self.password = tk.StringVar()

        labelUsername = tk.Label(self, 
                                  text = 'Username',
                                  fg = 'blue')
        labelUsername.grid(row = 0, column = 0, sticky = 'n')

        labelPassword = tk.Label(self, 
                                  text = 'Password',
                                  fg = 'blue')
        labelPassword.grid(row = 1, column = 0, sticky = 'n')

        self.Tusername = ttk.Entry(self, textvariable = self.username)
        self.Tpassword = ttk.Entry(self, textvariable = self.password)

        self.Tusername.focus()
        self.Tpassword.focus()

        self.Tusername.grid(row = 0, column = 2, padx = (0.10))
        self.Tpassword.grid(row = 1, column = 2, padx = (0.10))

class Frame2(tk.Frame):
    def __init__(self, container, controller, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.configure(bg = 'red')

        self.username = tk.StringVar()

        labelUsername = tk.Label(self, 
                                  text = 'Username',
                                  fg = 'blue')
        labelUsername.grid(row = 0, column = 0, columnspan = 4, sticky = 'n')

        labelPassword = tk.Label(self, 
                                  text = 'Password',
                                  fg = 'blue')
        labelPassword.grid(row = 1, column = 0, sticky = 'n')
        


myapp = App()
myapp.mainloop()