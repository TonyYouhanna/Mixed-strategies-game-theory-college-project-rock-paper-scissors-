import random
from tkinter import *
from tkinter import Radiobutton
from tkinter import messagebox

main = Tk()
main.title("Rock-Paper-Scissors")
numOfPlayersLabel = Label(main, text="choose number of players:")
numOfPlayersLabel.grid(row=0, column=0)
numPlayersBool = IntVar(main, value=0)
onePlayerRB = Radiobutton(main, text="1 player", variable=numPlayersBool, value=1)
twoPlayersRB = Radiobutton(main, text="2 players", variable=numPlayersBool, value=2)
onePlayerRB.grid(row=0, column=1)
twoPlayersRB.grid(row=0, column=2)
p1choiceBool = IntVar(main, value=0)
p2choiceBool = IntVar(main, value=0)
p1score1 = 0
p1score2 = 0
p2score = 0
pcScore = 0


def shoot1():
    pcChoice = random.choice([1, 2, 3])
    print(pcChoice)
    print(type(pcChoice))
    print(p1choiceBool.get())
    global p1score1
    global pcScore
    if p1choiceBool.get() == 0:
        messagebox.showerror("Error", "You have to choose rock or paper or scissors")
    else:
        if pcChoice == p1choiceBool.get():
            p1score1 += 1
            pcScore += 1
        elif (pcChoice == 1) & (p1choiceBool.get() == 2):
            p1score1 += 1
        elif (pcChoice == 2) & (p1choiceBool.get() == 3):
            p1score1 += 1
        elif (pcChoice == 3) & (p1choiceBool.get() == 1):
            p1score1 += 1
        elif (pcChoice == 2) & (p1choiceBool.get() == 1):
            pcScore += 1
        elif (pcChoice == 3) & (p1choiceBool.get() == 2):
            pcScore += 1
        elif (pcChoice == 1) & (p1choiceBool.get() == 3):
            pcScore += 1
        p1scoreLabel = Label(main, text="Player 1 score:")
        p1scoreLabel.grid(row=4, column=0)
        p1scoreText = IntVar()
        p1scoreTextbox = Entry(main, textvariable=p1scoreText)
        p1scoreTextbox.grid(row=4, column=1)
        p1scoreText.set(p1score1)
        pcScoreLabel = Label(main, text="PC score:")
        pcScoreLabel.grid(row=5, column=0)
        pcScoreText = IntVar()
        pcScoreTextbox = Entry(main, textvariable=pcScoreText)
        pcScoreTextbox.grid(row=5, column=1)
        pcScoreText.set(pcScore)
        if (p1score1 == 3) & (pcScore == 3):
            messagebox.showinfo("Info", "Tie")
            p1score1 = 0
            pcScore = 0
            p1scoreText.set(p1score1)
            pcScoreText.set(pcScore)
        elif p1score1 == 3:
            messagebox.showinfo("Info", "You won")
            p1score1 = 0
            pcScore = 0
            p1scoreText.set(p1score1)
            pcScoreText.set(pcScore)
        elif pcScore == 3:
            messagebox.showinfo("Info", "You lost")
            p1score1 = 0
            pcScore = 0
            p1scoreText.set(p1score1)
            pcScoreText.set(pcScore)



def shoot2():
    global p1score2
    global p2score
    if (p2choiceBool.get() == 0) | (p1choiceBool.get() == 0):
        messagebox.showerror("Error", "You have to choose rock or paper or scissors")
    else:
        if p2choiceBool.get() == p1choiceBool.get():
            p1score2 += 1
            p2score += 1
        elif (p2choiceBool.get() == 1) & (p1choiceBool.get() == 2):
            p1score2 += 1
        elif (p2choiceBool.get() == 2) & (p1choiceBool.get() == 3):
            p1score2 += 1
        elif (p2choiceBool.get() == 3) & (p1choiceBool.get() == 1):
            p1score2 += 1
        elif (p2choiceBool.get() == 2) & (p1choiceBool.get() == 1):
            p2score += 1
        elif (p2choiceBool.get() == 3) & (p1choiceBool.get() == 2):
            p2score += 1
        elif (p2choiceBool.get() == 1) & (p1choiceBool.get() == 3):
            p2score += 1
        p1scoreLabel = Label(main, text="Player 1 score:")
        p1scoreLabel.grid(row=5, column=0)
        p1scoreText = IntVar()
        p1scoreTextbox = Entry(main, textvariable=p1scoreText)
        p1scoreTextbox.grid(row=5, column=1)
        p1scoreText.set(p1score2)
        p2scoreLabel = Label(main, text="Player 2 score:")
        p2scoreLabel.grid(row=6, column=0)
        p2scoreText = IntVar()
        p2scoreTextbox = Entry(main, textvariable=p2scoreText)
        p2scoreTextbox.grid(row=6, column=1)
        p2scoreText.set(p2score)
        if (p1score2 == 3) & (p2score == 3):
            messagebox.showinfo("Info", "Tie")
            p1score2 = 0
            p2score = 0
            p1scoreText.set(p1score2)
            p2scoreText.set(p2score)
        elif p1score2 == 3:
            messagebox.showinfo("Info", "Player 1 won")
            p1score2 = 0
            p2score = 0
            p1scoreText.set(p1score2)
            p2scoreText.set(p2score)
        elif p2score == 3:
            messagebox.showinfo("Info", "Player 2 won")
            p1score2 = 0
            p2score = 0
            p1scoreText.set(p1score2)
            p2scoreText.set(p2score)


def start():
    if numPlayersBool.get() == 1:
        player1choiceLabel = Label(main, text="Player 1 choice:")
        player1choiceLabel.grid(row=2, column=0)
        rock1RB = Radiobutton(main, text="rock", variable=p1choiceBool, value=1)
        paper1RB = Radiobutton(main, text="paper", variable=p1choiceBool, value=2)
        scissors1RB = Radiobutton(main, text="scissors", variable=p1choiceBool, value=3)
        rock1RB.grid(row=2, column=1)
        paper1RB.grid(row=2, column=2)
        scissors1RB.grid(row=2, column=3)
        shoot1button = Button(main, text="Shoot", command=shoot1)
        shoot1button.grid(row=3, column=0)
    elif numPlayersBool.get() == 2:
        player1choiceLabel = Label(main, text="Player 1 choice:")
        player1choiceLabel.grid(row=2, column=0)
        rock1RB = Radiobutton(main, text="rock", variable=p1choiceBool, value=1)
        paper1RB = Radiobutton(main, text="paper", variable=p1choiceBool, value=2)
        scissors1RB = Radiobutton(main, text="scissors", variable=p1choiceBool, value=3)
        rock1RB.grid(row=2, column=1)
        paper1RB.grid(row=2, column=2)
        scissors1RB.grid(row=2, column=3)
        player2choiceLabel = Label(main, text="Player 2 choice:")
        player2choiceLabel.grid(row=3, column=0)
        rock2RB = Radiobutton(main, text="rock", variable=p2choiceBool, value=1)
        paper2RB = Radiobutton(main, text="paper", variable=p2choiceBool, value=2)
        scissors2RB = Radiobutton(main, text="scissors", variable=p2choiceBool, value=3)
        rock2RB.grid(row=3, column=1)
        paper2RB.grid(row=3, column=2)
        scissors2RB.grid(row=3, column=3)
        shoot2button = Button(main, text="Shoot", command=shoot2)
        shoot2button.grid(row=4, column=0)


startButton = Button(main, text="Start", command=start)
startButton.grid(row=1, column=0)
mainloop()
