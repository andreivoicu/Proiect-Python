from tkinter import *
from PIL import Image, ImageTk
import GlobalVariables as var


class SettingsWindow(Toplevel):

    def __init__(self, master):
        super().__init__(master=master)
        self.title("Settings")
        self.geometry("800x600")

        def changeTime():
            timeInput = timeText.get("1.0", "end-1c")
            var.setTime(int(timeInput))
            print(var.getTime())

        def changeDifficulty():
            var.setDifficulty(clicked.get())
            print(var.getDifficulty())

        # Button to return to main menu

        backButton = Button(self, text="<-")
        backButton.bind("<Button>", lambda e: [self.destroy(), master.update(), master.deiconify()])
        backButton.place(relx=0, rely=0, anchor=NW, height=20, width=50)

        # labels for time&difficulty

        timelabel = Label(self, text='set time', font=('comic', 30, 'italic bold'), fg='black')
        timelabel.place(relx=0.35, rely=0.45, anchor=CENTER, height=70, width=200)

        difficultylabel = Label(self, text='set difficulty', font=('comic', 30, 'italic bold'), fg='black')
        difficultylabel.place(relx=0.35, rely=0.55, anchor=CENTER, height=70, width=200)

        # text box for user to input time

        timeText = Text(self, height=1, width=3, bg='light cyan', font=('comic', 20, 'italic bold'))
        timeText.place(relx=0.55, rely=0.45, anchor=CENTER)

        # drop down list for user to select difficulty

        options = ['Easy', 'Medium', 'Hard']
        clicked = StringVar()
        clicked.set('Medium')

        drop = OptionMenu(self, clicked, *options)
        drop.place(relx=0.55, rely=0.55, anchor=CENTER)

        # buttons for changes to be saved

        timeSet = Button(self, text='Set')
        timeSet.bind("<Button>", lambda e: changeTime())
        timeSet.place(relx=0.65, rely=0.45, anchor=CENTER)

        difficultySet = Button(self, text="Set")
        difficultySet.bind("<Button>", lambda e: changeDifficulty())
        difficultySet.place(relx=0.65, rely=0.55, anchor=CENTER)

