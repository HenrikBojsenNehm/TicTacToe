#imports
#----------------------------------------------------------------
import tkinter as tk
import time
import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import Gamemodes
#------------------------------|imports|-------------------------

#gloabal variables
#----------------------------------------------------------------
gameMode = 0
solo = bool
score = {'xWins': 0, 'oWins': 0, 'draws': 0}
images = {}
assets = []
#----------------------------|gloabal variables|-----------------

#import the images
#----------------------------------------------------------------
imageOpen_0 = Image.open(os.path.join(os.getcwd(), 'TicTacToe\Assets\empty.png').replace('\\', '/'))
image_0 = imageOpen_0.resize((175,175), Image.Resampling.LANCZOS).convert(mode='RGBA')
images[0] = image_0

imageOpen_1 = Image.open(os.path.join(os.getcwd(), 'TicTacToe\Assets\imageX.png').replace('\\', '/'))
image_1 = imageOpen_1.resize((175,175), Image.Resampling.LANCZOS).convert(mode='RGBA')
images[1] = image_1

imageOpen_2 = Image.open(os.path.join(os.getcwd(), 'TicTacToe\Assets\imageO.png').replace('\\', '/'))
image_2 = imageOpen_2.resize((175,175), Image.Resampling.LANCZOS).convert(mode='RGBA')
images[2] = image_2
#-----------------------------|import the images|----------------

#Clear all widgets
#----------------------------------------------------------------
def clearScreen(master):
    for widgets in master.winfo_children():
        widgets.destroy()
#-------------------------------|Clear all widgets|--------------


#the app
#----------------------------------------------------------------
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.startUp()
    

    #start up
    #----------------------------------------------------------------
    def startUp(self):
        selfMaster = self.master
        selfMaster.title('Tic tac toe')
        self.mainMenu(selfMaster)
        
        for i in images :
            assets.append(ImageTk.PhotoImage(images[i]))
    #------------------------------|start up|------------------------
    
    #main menu
    #----------------------------------------------------------------
    def mainMenu(self, master):
        for i in score :
            score[i] = 0
        clearScreen(master)

        master.geometry('600x400')
        underTxt = StringVar()

        print('Menu started')

        title = Label(master, text='TicTacToe!', font=('Helvetica', 30))
        underTitle = Label(master, textvariable=underTxt, font=('Helvetica',20))
        title.pack(pady=15)
        underTitle.pack(pady=10)
        
        underTxt.set('Select gamemode')

        def gamemode(gameModeVal):
            for widget in master.winfo_children():
                if widget == quitGameBtn:
                    widget.pack_forget()
                elif isinstance(widget, tk.Button):
                    widget.destroy();
            global gameMode
            gameMode = gameModeVal
            mode1 = Button(master, text='Singleplayer', command=lambda:(runSolo()), font=('Helvetica', 15))
            mode2 = Button(master, text='Multiplayer', command=lambda:(runMulti()), font=('Helvetica', 15))
            underTxt.set('Select mode')
            mode1.pack(pady=5)
            mode2.pack(pady=5)
            quitGameBtn.pack(pady=5)
        

        def runSolo():
            global solo
            solo = True
            self.startGame(master)
        
        def runMulti():
            global solo
            solo = False
            messagebox.showinfo('TicTacToe', 'Work in progress')
            print("WORK IN PROGRESS")
            self.startGame(master)

        gamemodeBtn1 = Button(master, text='Tic Tac Toe', command=lambda:(gamemode(1)), font=('Helvetica', 15))
        gamemodeBtn1.pack(pady=5)
        #gamemodeBtn2 = Button(master, text='Ultimate Tic Tac Toe', command=lambda:(gamemode(2)), font=('Helvetica', 15))
        #gamemodeBtn2.pack(pady=5)
        quitGameBtn = Button(master, text='Quit', command=master.destroy, font=('Helvetica', 15))
        quitGameBtn.pack(pady=5)
    #--------------------------|main menu|---------------------------

    #end of round menu
    #----------------------------------------------------------------
    def endOfRoundMenu(self, gameWon, drawNum, master) :
        global gameMode, solo
        if gameWon != 0 or drawNum==0 :
            print('End of round menu start')
            time.sleep(0.25)
            whoWonTxt = StringVar()
            endMenuFrame = Frame(master)
            endMenuFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
            if gameWon==1 :
                score['xWins'] += 1
                whoWonTxt.set('X has won this round')
            elif gameWon==2 :
                score['oWins'] += 1
                whoWonTxt.set('O has won this round')
            elif drawNum==0 :
                score['draws'] += 1
                whoWonTxt.set('Draw')
            else :
                whoWonTxt.set('ERROR')
            print(f'{whoWonTxt.get()} the current score is: {score}')
            whoWon = Label(endMenuFrame, textvariable=whoWonTxt, font=('Helvetica', 20))
            replayBtn = Button(endMenuFrame, text='Play another round', font=('Helvetica', 15), command=lambda:(
                time.sleep(0.25),
                self.startGame(master)))
            backToMenuBtn = Button(endMenuFrame, text='Menu', font=('Helvetica', 15), command=lambda:(
                time.sleep(0.25),
                self.mainMenu(master)))
            whoWon.pack(pady=30, padx=15)
            replayBtn.pack(pady=15, padx=15)
            backToMenuBtn.pack(pady=15, padx=15)

        #-----------------------|end of round menu|----------------------

    #start the game
    #----------------------------------------------------------------
    def startGame(self, master):

        global gameMode, solo

        master.geometry('')
        clearScreen(master)
        
        if gameMode == 1:
            Gamemode = Gamemodes.TicTacToe
        elif gameMode == 2:
            Gamemode = Gamemodes.UltimateTicTacToe
        else:
            print('MODE SELECTION EROR')
            return

        Gamemode.run(self, master, assets)

        if(solo==True):
            print('Are you okay?')
        else:
            print('Ok!')

        round = 1
        for value in score :
            round += int(score[value])

        roundTxt = f'Round {round}'
        roundLbl = Label(master, text=roundTxt, font=('Helvetica', 20))
        roundLbl.grid(row=0, column=1, pady=15, padx=15)

    #---------------------------------|start the game|-------------------        

#--------------------------------|the app|-----------------------

#run the app
#----------------------------------------------------------------
root = tk.Tk()
app = App(master=root)
app.mainloop()
#---------------------------------|run the app|------------------