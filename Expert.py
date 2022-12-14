from words import words
from tkinter import *
import random
import tkinter.font as font
from tkinter import messagebox

TB = Tk()
TB.geometry('950x600')
TB.title("areTyping Test")
TB.config(bg='LightBlue1')

TB.attributes('-fullscreen', True)

headingFrame1 = Frame(TB, bg="snow3", bd=5)
headingFrame1.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Beginner Typing Speed Test", bg='azure2', fg='black',
                     font=('Courier', 15, 'bold'))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn = Button(TB, text="Start", bg='old lace', fg='black', width=20, height=2, command=TB.destroy,
             font=font.Font(size=15))
btn.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.10)

TB.mainloop()

CS= Tk()
CS.geometry('950x600')
CS.title('Beginner Typing Speed Test')
CS.config(bg="orange")

CS.attributes('-fullscreen', True)

score = 0
missed = 0
time = 60
count1 = 0
Total = 0
movingwords = ''

btn = Button(CS, text="X", bg='red', fg='black', command=CS.destroy,
             font=font.Font(size=15))
btn.place(relx=0.95, rely=0.95, relwidth=0.02, relheight=0.03)

def movingtext():
    global count1,movingwords
    floatingtext='Type Speed Test'
    if count1>= len(floatingtext):
        count1 =0
        movingwords =''
    movingwords += floatingtext[count1]
    count1 +=1
    fontlabel.configure(text=movingwords)
    fontlabel.after(250, movingtext)


def giventime():
    global time, score, missed, Total
    if time > 11:
        pass
    else:
        timercount.configure(fg='red')
    if time > 0:
        time -= 1
        timercount.configure(text=time)
        timercount.after(1000, giventime)
    else:
        gameinstruction.configure(text='Hit = {} | Miss = {} | Total Score = {} | accuracy = {}%'
                                  .format((score+missed), missed, Total,str(round((score/(score+missed))*100,2))))
        rr= messagebox.askretrycancel('Notification', 'Do you want to play again?')
        if rr==True:
            score = 0
            missed = 0
            time = 60
            timercount.configure(text=time)
            labelforward.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)

        if rr == False:
            score = 0
            missed = 0
            time = 60
            timercount.configure(text=time)
            labelforward.configure(text=words[0])
            scorelabelcount.configure(text=score)
            wordentry.delete(0, END)
            

def game(event):
    global score, missed, Total
    if time==60:
        giventime()
    gameinstruction.configure(text='')
    startlabel.configure(text='')
    if wordentry.get()== labelforward['text']:
        score +=1
        scorelabelcount.configure(text=score)
    else:
        missed +=1
    random.shuffle(words)
    labelforward.configure(text=words[0])
    wordentry.delete(0,END)

    if score>=0:
        Total = score - missed
        if Total<0:
            Total = 0

        wordentry.delete(0, END)
fontlabel=Label(CS,text='',font=('Imprint MT Shadow',25
                ),fg='purple',width=40)
fontlabel.place(relx=0, rely=0, relwidth=1, relheight=0.1)
movingtext()

startlabel = Label(CS, text='Start Typing', font=('arial', 30, 'italic bold'), bg='orange', fg='white')
startlabel.place(relx=0.35, rely=0.525, relwidth=0.3, relheight=0.1)

random.shuffle(words)
labelforward = Label(CS, text=words[0], font=('arial', 45, 'bold'),bg='yellow', fg='green')
labelforward.place(relx=0.325, rely=0.35, relwidth=0.35, relheight=0.15)


scorelabel=Label(CS, text='Your Score:',font=('arial', 25, 'bold'), fg='red')
scorelabel.place(relx=0.025, rely=0.125, relwidth=0.25, relheight=0.075)

scorelabelcount=Label(CS, text=score, font=('arial', 25, 'bold'), fg='blue')
scorelabelcount.place(relx=0.025, rely=0.2, relwidth=0.25, relheight=0.075)

labelfortimer=Label(CS, text='Time Left:', font=('arial', 25, 'bold'), fg='red')
labelfortimer.place(relx=0.725, rely=0.125, relwidth=0.25, relheight=0.075)

timercount=Label(CS, text=time, font=('arial', 25, 'bold'), fg='blue')
timercount.place(relx=0.725, rely=0.2, relwidth=0.25, relheight=0.075)

gameinstruction = Label(CS, text='Hit enter button after typing the word', font=('arial', 25, 'bold'),bg=
'orange', fg='black')
gameinstruction.place(relx=0.2, rely=0.85, relwidth=0.8, relheight=0.1)

wordentry = Entry(CS, font=('arial', 25, 'bold'), bd=10, justify='center')
wordentry.place(relx=0.3, rely=0.65, relwidth=0.4, relheight=0.1)
wordentry.focus_set()

CS.bind('<Return>', game)
mainloop()
