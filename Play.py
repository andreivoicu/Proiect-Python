from tkinter import *


class PlayWindow(Toplevel):

    def __init__(self, master):
        super().__init__(master=master)
        self.title("Play!")
        self.geometry("800x600")

        backButton = Button(self, text="<-")
        backButton.bind("<Button>", lambda e: [self.destroy(), master.update(), master.deiconify()])
        backButton.place(relx=0, rely=0, anchor=NW, height=20, width=50)

