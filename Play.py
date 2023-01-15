import random
from words import words
from tkinter import *
from tkinter import messagebox

score = 0
missed = 0
time = 60

class PlayWindow(Toplevel):

    def __init__(self, master):
        super().__init__(master=master)
        self.title("Play!")
        self.geometry("800x600")

        backButton = Button(self, text="<-")
        backButton.bind("<Button>", lambda e: [self.destroy(), master.update(), master.deiconify()])
        backButton.place(relx=0, rely=0, anchor=NW, height=20, width=50)

        def giventime():
            global time, score, missed
            if time > 11:
                pass
            else:
                timercount.configure(fg='red')
            if time > 0:
                time -= 1
                timercount.configure(text=time)
                timercount.after(1000, giventime)
            else:
                gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {}'
                                          .format(score, missed, score - missed))
                rr = messagebox.askretrycancel('Notification', 'Do you want to play again?')
                if rr == True:
                    score = 0
                    missed = 0
                    time = 60
                    timercount.configure(text=time)
                    labelforward.configure(text=words[0])
                    scorelabelcount.configure(text=score)
                    wordentry.delete(0, END)

        def game(event):
            global score, missed
            if time == 60:
                giventime()
            gameinstruction.configure(text='')
            startlabel.configure(text='')
            if wordentry.get() == labelforward['text']:
                score += 1
                scorelabelcount.configure(text=score)
            else:
                missed += 1
            random.shuffle(words)
            labelforward.configure(text=words[0])
            wordentry.delete(0, END)

        startlabel = Label(self, text='Start Typing', font=('arial', 30, 'italic bold'), bg='black', fg='white')
        startlabel.place(x=275, y=50)

        random.shuffle(words)
        labelforward = Label(self, text=words[0], font=('arial', 45, 'italic bold'), fg='green')
        labelforward.place(x=250, y=240)

        scorelabel = Label(self, text='Your Score:', font=('arial', 25, 'italic bold'), fg='red')
        scorelabel.place(x=10, y=100)

        scorelabelcount = Label(self, text=score, font=('arial', 25, 'italic bold'), fg='blue')
        scorelabelcount.place(x=150, y=180)

        labelfortimer = Label(self, text='Time Left:', font=('arial', 25, 'italic bold'), fg='red')
        labelfortimer.place(x=600, y=100)

        timercount = Label(self, text=time, font=('arial', 25, 'italic bold'), fg='blue')
        timercount.place(x=600, y=180)

        gameinstruction = Label(self, text='Hit enter button after typing the word',
                                font=('arial', 25, 'italic bold'), fg='grey')
        gameinstruction.place(x=150, y=500)

        wordentry = Entry(self, font=('arial', 25, 'italic bold'), bd=10, justify='center')
        wordentry.place(x=250, y=330)
        wordentry.focus_set()

        self.bind('<Return>', game)
