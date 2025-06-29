from tkinter import *
import random
import time as tm
windowmenu = Tk()
windowmenu.geometry('800x1000')
windowmenu.resizable("False","False")
windowmenu.title("Wood Guy")

gamewindow = Toplevel()
gamewindow.geometry('800x1000')
gamewindow.resizable("False","False")
gamewindow.title("Wood Guy")
gamewindow.withdraw()

losewindow = Toplevel()
losewindow.geometry('800x1000')
losewindow.resizable("False","False")
losewindow.title("Wood Guy")
losewindow.withdraw()

litera = ""
score = -2
scorestr = StringVar()

highscore = score
highscorestr = StringVar()
highscorestr.set("0")

Yobstacle_list = [185,50]  # im mniejsza wartosc, tym wyzej przeszkoda
Yobstacle1 = 0
Yobstacle2 = 0
Yobstacle3 = 0
Yobstacle4 = 0
Xobstacle_list = [445,225]  # 445 - przeszkoda po prawej, 225 - przeszkoda po lewej
Xobstacle1 = 0
Xobstacle2 = 0
Xobstacle3 = 0
Xobstacle4 = 0
XCharacter = 0

def startgame():
    windowmenu.withdraw()
    reset()
    gamewindow.deiconify()

def TreeProgress(x):
    if x == 1:
        Tree_label1.place(x=357,y=666)
        Tree_label2.place(x=357,y=533)
        Tree_label3.place(x=357,y=400)
        Tree_label4.place(x=357,y=267)
        Tree_label5.place(x=357,y=134)
        Tree_label6.place(x=357,y=1)
    elif x == 2:
        Tree_label1.place(x=357,y=1)
        Tree_label2.place(x=357,y=666)
        Tree_label3.place(x=357,y=533)
        Tree_label4.place(x=357,y=400)
        Tree_label5.place(x=357,y=267)
        Tree_label6.place(x=357,y=134)
    elif x == 3:
        Tree_label1.place(x=357,y=134)
        Tree_label2.place(x=357,y=1)
        Tree_label3.place(x=357,y=666)
        Tree_label4.place(x=357,y=533)
        Tree_label5.place(x=357,y=400)
        Tree_label6.place(x=357,y=267)

def ObsProgress():
    global Yobstacle1,Yobstacle2,Yobstacle3,Yobstacle4,Yobstacle_list,Xobstacle1,Xobstacle2,Xobstacle3,Xobstacle4,Xobstacle_list
    a = random.randint(1,4)
    if (Yobstacle1 == 50 or 185 or 320 or 455 or 590 or 725):
        Yobstacle1 = Yobstacle1 + 135
        ObstacleLabel1.place(x=Xobstacle1,y=Yobstacle1)
    if (Yobstacle1 > 725 and Yobstacle3 != 50 and Yobstacle2 != 50 and Yobstacle4 != 50 and a <= 2):
        Yobstacle1 = 50
        Xobstacle1 = random.choice(Xobstacle_list)
        ObstacleLabel1.place(x=Xobstacle1,y=Yobstacle1)
    elif (Yobstacle1 > 725):
        ObstacleLabel1.place_forget()
    
    if (Yobstacle2 == 50 or 185 or 320 or 455 or 590 or 725):
        Yobstacle2 = Yobstacle2 + 135
        ObstacleLabel2.place(x=Xobstacle2,y=Yobstacle2)
    if (Yobstacle2 > 725 and Yobstacle3 != 50 and Yobstacle1 != 50 and Yobstacle4 != 50 and a <= 2):
        Yobstacle2 = 50
        Xobstacle2 = random.choice(Xobstacle_list)
        ObstacleLabel2.place(x=Xobstacle2,y=Yobstacle2)
    elif (Yobstacle2 > 725):
        ObstacleLabel2.place_forget()
    
    if (Yobstacle3 == 0 and Yobstacle1 != 50 and Yobstacle2 != 50 and Yobstacle4 != 50 and a == 3):
        Yobstacle3 = 50
        Xobstacle3 = random.choice(Xobstacle_list)
        ObstacleLabel3.place(x=Xobstacle3,y=Yobstacle3)
    elif (Yobstacle3 == 50 or Yobstacle3 == 185 or Yobstacle3 == 320 or Yobstacle3 == 455 or Yobstacle3 == 590 or Yobstacle3 == 725):
        Yobstacle3 = Yobstacle3 + 135
        ObstacleLabel3.place(x=Xobstacle3,y=Yobstacle3)
    if (Yobstacle3 > 725 and Yobstacle1 != 50 and Yobstacle2 != 50 and Yobstacle4 != 50 and a == 3):
        Yobstacle3 = 50
        Xobstacle3 = random.choice(Xobstacle_list)
        ObstacleLabel3.place(x=Xobstacle3,y=Yobstacle3)
    elif (Yobstacle3 > 725):
        ObstacleLabel3.place_forget()

    if (Yobstacle4 == 0 and Yobstacle1 != 50 and Yobstacle2 != 50 and Yobstacle3 != 50 and a == 3):
        Yobstacle4 = 50
        Xobstacle4 = random.choice(Xobstacle_list)
        ObstacleLabel4.place(x=Xobstacle4,y=Yobstacle4)
    elif (Yobstacle4 == 50 or Yobstacle4 == 185 or Yobstacle4 == 320 or Yobstacle4 == 455 or Yobstacle4 == 590 or Yobstacle4 == 725):
        Yobstacle4 = Yobstacle4 + 135
        ObstacleLabel4.place(x=Xobstacle4,y=Yobstacle4)
    if (Yobstacle4 > 725 and Yobstacle1 != 50 and Yobstacle2 != 50 and Yobstacle3 != 50 and a == 3):
        Yobstacle4 = 50
        Xobstacle4 = random.choice(Xobstacle_list)
        ObstacleLabel4.place(x=Xobstacle4,y=Yobstacle4)
    elif (Yobstacle4 > 725):
        ObstacleLabel4.place_forget()

def LoseGame(x):
    global Yobstacle1,Yobstacle2,Yobstacle3,Yobstacle4,Xobstacle1,Xobstacle2,Xobstacle3,Xobstacle4
    if (x == 1):
        Yobstacle = Yobstacle1
        Xobstacle = Xobstacle1
    elif (x == 2):
        Yobstacle = Yobstacle2
        Xobstacle = Xobstacle2
    elif (x == 3):
        Yobstacle = Yobstacle3
        Xobstacle = Xobstacle3
    elif (x == 4):
         Yobstacle = Yobstacle4
         Xobstacle = Xobstacle4

    if (Yobstacle == 725):
        if (XCharacter == 158):
            if (Xobstacle == 225):
                print("przegrales (lewo)")
                tm.sleep(1)
                gamewindow.withdraw()
                losewindow.deiconify()
                reset()
        elif (XCharacter == 375):
            if (Xobstacle == 445):
                print("przegrales (prawo)")
                tm.sleep(1)
                gamewindow.withdraw()
                losewindow.deiconify()
                reset()

def onKeyPress(event):
    global litera,score,scorestr,Yobstacle1,Yobstacle2,Yobstacle3,Yobstacle4,Xobstacle1,Xobstacle2,Xobstacle3,Xobstacle4,XCharacter
    litera = event.char
    if (litera == "a"):
        XCharacter = 158
        TestCharacter_Label.place(x=XCharacter,y=590)
        score = score+1
        scorestr.set(eval(str(score)+"+1"))
        if (score%3 == 1):
            ObsProgress()
            TreeProgress(1)

        elif (score%3 == 2):
            ObsProgress()
            TreeProgress(2)

        else:
            ObsProgress()
            TreeProgress(3)

    elif (litera == "d"):
        XCharacter = 375
        TestCharacter_Label.place(x=XCharacter,y=590)
        score = score+1
        scorestr.set(eval(str(score)+"+1"))
        if (score%3 == 1):
            ObsProgress()
            TreeProgress(1)

        elif (score%3 == 2):
            ObsProgress()
            TreeProgress(2)

        else:
            ObsProgress()
            TreeProgress(3)
    LoseGame(1)
    LoseGame(2)
    LoseGame(3)
    LoseGame(4)
                 
def reset():
    global highscore,highscorestr,score,scorestr,Yobstacle1,Yobstacle2,Yobstacle3,Yobstacle4
    Tree_label1.place(x=357,y=666)
    Tree_label2.place(x=357,y=533)
    Tree_label3.place(x=357,y=400)
    Tree_label4.place(x=357,y=267)
    Tree_label5.place(x=357,y=134)
    Tree_label6.place(x=357,y=1)
    while(Yobstacle1 == 725 or Yobstacle2 == 725 or Yobstacle3 == 725 or Yobstacle4 == 725 or Yobstacle1 == 590 or Yobstacle2 == 590 or Yobstacle3 == 590 or Yobstacle4 == 590):
        ObsProgress()
    if (score > highscore):
        highscore = score
        highscorestr.set(eval(str(highscore)))
    score = -1
    scorestr.set(eval(str(score)+"+1"))

def QuitGame():
    windowmenu.destroy()

def PlayAgain():
    losewindow.withdraw()
    reset()
    gamewindow.deiconify()

def GoToMenu():
    losewindow.withdraw()
    reset()
    windowmenu.deiconify()

gamewindow.bind('<KeyPress>', onKeyPress)

FrameGameOver = Frame(losewindow,bg="green")
FrameGameOver.place(x=0,y=700,height=80,width=800)

FrameMain = Frame(windowmenu,bg="lime")
FrameMain.place(x=0,y=0,height=1000,width=800)

FrameStart = Frame(FrameMain,bg="Red")
FrameStart.place(x=0,y=700,height=80,width=800)

FrameButtons = Frame(FrameMain,bg="green")
FrameButtons.place(x=0,y=620,height=80,width=800)

FrameLeave1 = Frame(FrameMain,bg="blue")
FrameLeave1.place(x=0,y=920,height=80,width=800)

FrameLeave2 = Frame(losewindow,bg="blue")
FrameLeave2.place(x=0,y=920,height=80,width=800)

Frame_game = Frame(gamewindow)
Frame_game.place(x=0,y=25,height=975,width=800)

Frame_gamescore = Frame(gamewindow,bg="blue")
Frame_gamescore.place(x=0,y=0,height=40,width=800)

TestCharacter = PhotoImage(file="Test_Textures/test_character2.png")
TestCharacter_Label = Label(Frame_game, image=TestCharacter)

Tree_Log1 = PhotoImage(file="Textures/Tree_Log1.png")
Tree_Log2 = PhotoImage(file="Textures/Tree_Log2.png")
Tree_Log3 = PhotoImage(file="Textures/Tree_Log3.png")
Tree_Log4 = PhotoImage(file="Textures/Tree_Log4.png")
Tree_Log5 = PhotoImage(file="Textures/Tree_Log5.png")
Tree_Log6 = PhotoImage(file="Textures/Tree_Log6.png")

Branch1 = PhotoImage(file="Textures/branch1.png")
Branch2 = PhotoImage(file="Textures/branch2.png")

pixel=PhotoImage(width=1,height=1)  #pixel ulatwia zmiane rozmiaru przycisku startujacego

Logo = PhotoImage(file="Logo/Logo_final-2.png")

Tree_label1 = Label(Frame_game,image=Tree_Log1,borderwidth=0)
Tree_label2 = Label(Frame_game,image=Tree_Log2,borderwidth=0)
Tree_label3 = Label(Frame_game,image=Tree_Log3,borderwidth=0)
Tree_label4 = Label(Frame_game,image=Tree_Log4,borderwidth=0)
Tree_label5 = Label(Frame_game,image=Tree_Log5,borderwidth=0)
Tree_label6 = Label(Frame_game,image=Tree_Log6,borderwidth=0)

ObstacleLabel1 = Label(Frame_game,image=Branch1,borderwidth=0)
ObstacleLabel2 = Label(Frame_game,image=Branch2,borderwidth=0)
ObstacleLabel3 = Label(Frame_game,image=Branch1,borderwidth=0)
ObstacleLabel4 = Label(Frame_game,image=Branch2,borderwidth=0)

score_count = Label(Frame_gamescore,textvariable=scorestr,font=("Comic Sans MS",24,"bold","italic"),image=pixel,compound="c",height=40,width=200)
score_count.place(x=295)

highscore_countMenu1 = Label(FrameMain, textvariable=highscorestr,font=("Comic Sans MS",24,"bold","italic"),image=pixel,compound="c",height=50,width=300)
highscore_countMenu1.place(x=400,y=410)
highscore_countMenu2 = Label(FrameMain, text="Highscore:",font=("Comic Sans MS",24,"bold","italic"),image=pixel,compound="c",height=50,width=165)
highscore_countMenu2.place(x=200,y=410)

highscore_countGameOver1 = Label(losewindow,textvariable=highscorestr,font=("Comic Sans MS",24,"bold","italic"),image=pixel,compound="c",height=50,width=300)
highscore_countGameOver1.place(x=400,y=600)
highscore_countGameOver2 = Label(losewindow,text="Highscore:",font=("Comic Sans MS",24,"bold","italic"),image=pixel,compound="c",height=50,width=165)
highscore_countGameOver2.place(x=200,y=600)

LogoLabel1 = Label(FrameMain,image=Logo)
LogoLabel1.place(x=-101)

LogoLabel2 = Label(losewindow,image=Logo)
LogoLabel2.place(x=-101)

pixel=PhotoImage(width=1,height=1)
BtnStart = Button(FrameStart,text="Start Game",font=("Comic Sans MS",18,"bold"),image=pixel,compound="c",height=80,width=200,command=lambda:startgame())
BtnStart.place(x=295,y=0)

BtnSkins = Button(FrameButtons,text="Customization\nComing Soon",font=("Comic Sans MS",18,"bold"),image=pixel,compound="c",height=80,width=200,state="disabled")
BtnSkins.place(x=550,y=0)

BtnModes = Button(FrameButtons,text="Modes\nComing Soon",font=("Comic Sans MS",18,"bold"),image=pixel,compound="c",height=80,width=200,state="disabled")
BtnModes.place(x=40,y=0)

BtnLeave1 = Button(FrameLeave1,text="Quit Game",font=("Comic Sans MS",18,"bold"),image=pixel,compound="c",height=80,width=200,command=lambda:QuitGame())
BtnLeave1.place(x=600,y=0)

BtnLeave2 = Button(FrameLeave2,text="Quit Game",font=("Comic Sans MS",18,"bold"),image=pixel,compound="c",height=80,width=200,command=lambda:QuitGame())
BtnLeave2.place(x=600,y=0)

BtnPlayAgain = Button(FrameGameOver,text="Play Again",font=("Comic Sans MS",18,"bold"),image=pixel,compound="c",height=80,width=200,command=lambda:PlayAgain())
BtnPlayAgain.place(x=195,y=0)

BtnGoBack = Button(FrameGameOver,text="Go Back To \nMain Menu",font=("Comic Sans MS",18,"bold"),image=pixel,compound="c",height=80,width=200,command=lambda:GoToMenu())
BtnGoBack.place(x=395,y=0)

if (Yobstacle1 == 0 and Yobstacle2 == 0):
    while(Yobstacle1 == Yobstacle2):
        Yobstacle1 = random.choice(Yobstacle_list)
        Yobstacle2 = random.choice(Yobstacle_list)
    Xobstacle1 = random.choice(Xobstacle_list)
    Xobstacle2 = random.choice(Xobstacle_list)
    ObstacleLabel1.place(x=Xobstacle1,y=Yobstacle1)
    ObstacleLabel2.place(x=Xobstacle2,y=Yobstacle2)

windowmenu.mainloop()