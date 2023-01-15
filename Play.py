import random
import words
from tkinter import *
from tkinter import messagebox
import GlobalVariables as var
from PIL import Image, ImageTk

currentScore = 0
currentMissed = 0
currentTime = 0
currentDifficulty = "Normal"
wordList = []


class PlayWindow(Toplevel):

    def __init__(self, master):
        super().__init__(master=master)
        self.title("Play!")
        self.geometry("800x600")
        bg = ImageTk.PhotoImage(file="home menu background.png")  # background for homePage

        self.canvas = Canvas(master, width=800, height=600)
        self.background_image = ImageTk.PhotoImage(file="home menu background.png")
        self.background_label = Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1, anchor='nw')
        
    
       
        backButton = Button(self, text="<-")
        backButton.bind("<Button>", lambda e: [self.destroy(), master.update(), master.deiconify()])
        backButton.place(relx=0, rely=0, anchor=NW, height=20, width=50)

        global currentTime, currentScore, currentMissed, currentDifficulty, wordList
        currentTime = var.getTime()
        currentScore = var.getScore()
        currentMissed = var.getMissed()
        currentDifficulty = var.getDifficulty()

        if currentDifficulty == "Easy":
            wordList = words.getEasy()
        elif currentDifficulty == "Medium":
            wordList = words.getMedium()
        elif currentDifficulty == "Hard":
            wordList = words.getHard()

        def giventime():
            global currentScore, currentMissed, currentTime
            if currentTime > 11:
                pass
            else:
                timercount.configure(fg='red')
            if currentTime > 0:
                currentTime -= 1
                timercount.configure(text=currentTime)
                timercount.after(1000, giventime)
            else:
                gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {}'
                                          .format(currentScore, currentMissed, currentScore - currentMissed))
                rr = messagebox.askretrycancel('Notification', 'Do you want to play again?')
                if rr:
                    currentScore = 0
                    currentMissed = 0
                    currentTime = var.getTime()
                    timercount.configure(text=currentTime)
                    labelforward.configure(text=words[0])

                    scorelabelcount.configure(text=currentScore)
                    gameinstruction(text = '')
                    wordentry.delete(0, END)

        def game(event):
            global currentScore, currentMissed
            if currentTime == var.getTime():
                giventime()
            gameinstruction.configure()
            scorelabel.configure(text = "Your Score:")
            scorelabelcount.configure(text = score)
            labelfortimer.configure(text = "Time Left:")
            timercount.configure(text = time)
            startlabel.destroy()
            if wordentry.get() == labelforward['text']:
                currentScore += 1
                scorelabelcount.configure(text=currentScore)
            else:
                currentMissed += 1
            random.shuffle(wordList)
            labelforward.configure(text=wordList[0])
            wordentry.delete(0, END)

        startlabel = Label(self, text='Start Typing', font=('arial', 45, 'italic bold'), fg='black')
        startlabel.place(relx=0.5, rely=0.25, anchor=CENTER)

        random.shuffle(words)
        labelforward = Label(self, text=words[0], font=('arial', 45, 'italic bold'), fg='green')
        labelforward.place(relx=0.5, rely = 0.40, anchor=CENTER)

        scorelabel = Label(self, font=('arial', 25, 'italic bold'), fg='red')
        scorelabel.place(x=50, y=100)

        scorelabelcount = Label(self, font=('arial', 25, 'italic bold'), fg='blue')
        scorelabelcount.place(x=250, y=100)

        labelfortimer = Label(self, font=('arial', 25, 'italic bold'), fg='red')
        labelfortimer.place(x=500, y=100)

        timercount = Label(self, font=('arial', 25, 'italic bold'), fg='blue')
        timercount.place(x=665, y=100)

        gameinstruction = Label(self, text='Hit enter button after typing the word',
                                font=('arial', 25, 'italic bold'), fg='grey')
        gameinstruction.place(relx= 0.5, rely=0.90, anchor=CENTER)

        wordentry = Entry(self, font=('arial', 25, 'italic bold'), bd=10, justify='center')
        wordentry.place(relx=0.5, rely=0.55, anchor=CENTER)
        wordentry.focus_set()

        self.bind('<Return>', game)
