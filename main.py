# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter import font

from PIL import Image, ImageTk
from tkinter.ttk import *

# creates a Tk() object
master = Tk()
master.title('speed typer')
master.config(bg="orange")
master.geometry("800x600")

helv36 = font.Font(family='Comic', size=36, weight='bold')

bg = ImageTk.PhotoImage(file="home menu background.png")

canvas1 = Canvas(master, width=800, height=600)
canvas1.pack(fill="both", expand=True)

canvas1.create_image(0, 0, image=bg, anchor="nw")

# Create style Object
style = Style()

style.configure('TButton', font=('Comic', 20, 'bold'))

# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground=[('active', '!disabled', 'green')],
          background=[('active', 'black')])

# Buttons

play = Button(master, text="Play")

play.place(relx=0.5, rely=0.25, anchor=N, height=70, width=170)

settings = Button(master, text="Settings")
settings.place(relx=0.5, rely=0.5, anchor=CENTER, height=70, width=170)

quit = Button(master, text="Quit", command=master.quit)
quit.place(relx=0.5, rely=0.75, anchor=S, height=70, width=170)

# mainloop, runs infinitely
mainloop()
