import random
import words
from tkinter import *
from tkinter import messagebox
import GlobalVariables as var

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
                    wordentry.delete(0, END)

        def game(event):
            global currentScore, currentMissed
            if currentTime == var.getTime():
                giventime()
            gameinstruction.configure(text='')
            startlabel.configure(text='')
            if wordentry.get() == labelforward['text']:
                currentScore += 1
                scorelabelcount.configure(text=currentScore)
            else:
                currentMissed += 1
            random.shuffle(wordList)
            labelforward.configure(text=wordList[0])
            wordentry.delete(0, END)

        startlabel = Label(self, text='Start Typing', font=('arial', 30, 'italic bold'), bg='black', fg='white')
        startlabel.place(x=275, y=50)

        random.shuffle(wordList)
        labelforward = Label(self, text=wordList[0], font=('arial', 45, 'italic bold'), fg='green')
        labelforward.place(x=250, y=240)

        scorelabel = Label(self, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
        scorelabel.place(x=10, y=100)

        scorelabelcount = Label(self, text=currentScore, font=('arial', 25, 'italic bold'), fg='blue')
        scorelabelcount.place(x=150, y=180)

        labelfortimer = Label(self, text='Time Left:', font=('arial', 25, 'italic bold'), fg='red')
        labelfortimer.place(x=600, y=100)

        timercount = Label(self, text=currentTime, font=('arial', 25, 'italic bold'), fg='blue')
        timercount.place(x=600, y=180)

        gameinstruction = Label(self, text='Hit enter button after typing the word',
                                font=('arial', 25, 'italic bold'), fg='grey')
        gameinstruction.place(x=150, y=500)

        wordentry = Entry(self, font=('arial', 25, 'italic bold'), bd=10, justify='center')
        wordentry.place(x=250, y=330)
        wordentry.focus_set()

        self.bind('<Return>', game)
