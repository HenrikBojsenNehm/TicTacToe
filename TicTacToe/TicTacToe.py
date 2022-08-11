#imports
#----------------------------------------------------------------
from ast import Global
from asyncio.windows_events import NULL
from pydoc import cli
import tkinter as tk
import time

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
#------------------------------|imports|-------------------------

#gloabal variables
#----------------------------------------------------------------
xTurn = True 
count = 0
gameWon = 0
buttons = []
buttonMatrix = []
#----------------------------|gloabal variables|-----------------

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
    #------------------------------|start up|------------------------
    
    #main menu
    #----------------------------------------------------------------
    def mainMenu(self, master):
        clearScreen(master)

        master.geometry('600x400')
        underTxt = StringVar()
        gamemode = 0

        print('Menu started')

        title = Label(master, text='TicTacToe!', font=('Helvetica', 30))
        underTitle = Label(master, textvariable=underTxt, font=('Helvetica',20))
        title.pack(pady=5)
        underTitle.pack(pady=10)
        
        underTxt.set('Select gamemode')

        def gamemode1(gamemode):
            for widget in master.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.destroy();
            gamemode = 1
            mode1 = Button(master, text='Singleplayer', command=lambda:(runSolo(gamemode)), font=('Helvetica', 15))
            mode2 = Button(master, text='Multiplayer', command=lambda:(runMulti(gamemode)), font=('Helvetica', 15))
            underTxt.set('Select mode')
            mode1.pack(pady=5)
            mode2.pack(pady=5)
            return gamemode

        def runSolo(gamemode):
            if gamemode == 1:
                self.startGame(True, master)
            else:
                print('MODE SELECTION EROR')
                return
        
        def runMulti(gamemode):
            messagebox.showinfo('TicTacToe', 'Work in progress')
            print("WORK IN PROGRESS")
            if gamemode == 1:
                return
            else:
                print('MODE SELECTION EROR')
                return

        gamemodeBtn1 = Button(master, text='Tic Tac Toe', command=lambda:(gamemode1(gamemode)), font=('Helvetica', 15))
        gamemodeBtn1.pack(pady=5)
    #--------------------------|main menu|---------------------------

    #start the game
    #----------------------------------------------------------------
    def startGame(self, solo, master):
        master.geometry('')
        clearScreen(master)
        
        if(solo==True):
            print('Are you okay?')
        else:
            print('Ok!')
        
        #import the images
        #----------------------------------------------------------------
        imageOpen_0 = Image.open('D:\Work\Python\TicTacToe.Py\TicTacToe\Assets\empty.png')
        image_0 = imageOpen_0.resize((175,175), Image.ANTIALIAS)
        img_0 = ImageTk.PhotoImage(image_0)

        imageOpen_1 = Image.open('D:\Work\Python\TicTacToe.Py\TicTacToe\Assets\imageX.png')
        image_1 = imageOpen_1.resize((175,175), Image.ANTIALIAS)
        img_1 = ImageTk.PhotoImage(image_1)

        imageOpen_2 = Image.open('D:\Work\Python\TicTacToe.Py\TicTacToe\Assets\imageO.png')
        image_2 = imageOpen_2.resize((175,175), Image.ANTIALIAS)
        img_2 = ImageTk.PhotoImage(image_2)
        #-----------------------------|import the images|----------------

        #button clicked function
        #----------------------------------------------------------------
#        def b_click(b):
#            global xTurn, count, gameWon
#            if gameWon!=0 :
#                pass
#            if b['image']=='pyimage1' and xTurn==True:
#                b['image']=img_1; b.image=img_1
#                xTurn=False
#                count+=1
#            elif b['image']=='pyimage1' and xTurn==False:
#                b['image']=img_2; b.image=img_2
#                xTurn=True
#                count+=1
#            else:
#                messagebox.showerror('TicTacToe', 'The box is already in use.\npick another box...')
        #-------------------------|button clicked function|---------------
            
            #check if win
            #----------------------------------------------------------------
        def gameStatus() :
            gameBox = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            global gameWon, buttons, buttonMatrix
            for button in buttons :
                y = button.grid_info()['row']
                x = button.grid_info()['column']
                buttonMatrix[y][x] = button
                if '1' in button['image'] :
                    gameBox[y][x] = 0
                elif '2' in button['image'] :
                    gameBox[y][x] = 1
                elif '3' in button['image'] :
                    gameBox[y][x] = 2
                    

                #check per row
                #----------------------------------------------------------------
                if gameBox[y][0]!=0 and gameBox[y][0]==gameBox[y][1] and gameBox[y][0]==gameBox[y][2]:
                    if gameBox[y][0]==1 :
                        gameWon = 1
                        print('X wins!')
                    elif gameBox[y][0]==2 :
                        gameWon = 2
                        print('O wins!')
                    if gameWon!=0 :
                        buttonMatrix[y][0]['bg'] = '#00ff00'; buttonMatrix[y][0]['activebackground'] = '#00ff00'
                        buttonMatrix[y][1]['bg'] = '#00ff00'; buttonMatrix[y][1]['activebackground'] = '#00ff00'
                        buttonMatrix[y][2]['bg'] = '#00ff00'; buttonMatrix[y][2]['activebackground'] = '#00ff00'
                #----------------------------|check per row|----------------------
                
                #check per column
                #----------------------------------------------------------------
                elif gameBox[0][x]!=0 and gameBox[0][x]==gameBox[1][x] and gameBox[0][x]==gameBox[2][x]:
                    if gameBox[0][x]==1 :
                        gameWon = 1
                        print('X wins!')
                    elif gameBox[0][x]==2 :
                        gameWon = 2
                        print('O wins!')
                    if gameWon!=0 :
                        buttonMatrix[0][x]['bg'] = '#00ff00'; buttonMatrix[0][x]['activebackground'] = '#00ff00'
                        buttonMatrix[1][x]['bg'] = '#00ff00'; buttonMatrix[1][x]['activebackground'] = '#00ff00'
                        buttonMatrix[2][x]['bg'] = '#00ff00'; buttonMatrix[2][x]['activebackground'] = '#00ff00'
                #-------------------------|check per column|-----------------------
                
                #check per diagonal
                #----------------------------------------------------------------
                elif gameBox[0][0]!=0 and gameBox[0][0]==gameBox[1][1] and gameBox[0][0]==gameBox[2][2]:
                    if gameBox[0][0]==1 :
                        gameWon = 1
                        print('X wins!')
                    elif gameBox[0][0]==2 :
                        gameWon = 2
                        print('O wins!')
                    if gameWon!=0 :
                        buttonMatrix[0][0]['bg'] = '#00ff00'; buttonMatrix[0][0]['activebackground'] = '#00ff00'
                        buttonMatrix[1][1]['bg'] = '#00ff00'; buttonMatrix[1][1]['activebackground'] = '#00ff00'
                        buttonMatrix[2][2]['bg'] = '#00ff00'; buttonMatrix[2][2]['activebackground'] = '#00ff00'
                elif gameBox[0][2]!=0 and gameBox[0][2]==gameBox[1][1] and gameBox[0][2]==gameBox[2][0]:
                    if gameBox[0][2]==1 :
                        gameWon = 1
                        print('X wins!')
                    elif gameBox[0][2]==2 :
                        gameWon = 2
                        print('O wins!')
                    if gameWon!=0 :
                        buttonMatrix[0][2]['bg'] = '#00ff00'; buttonMatrix[0][2]['activebackground'] = '#00ff00'
                        buttonMatrix[1][1]['bg'] = '#00ff00'; buttonMatrix[1][1]['activebackground'] = '#00ff00'
                        buttonMatrix[2][0]['bg'] = '#00ff00'; buttonMatrix[2][0]['activebackground'] = '#00ff00'
                #-------------------------------|check per diagonal|-------------------

            #-------------------------------|check if win|-------------------


            #announce winner
            #----------------------------------------------------------------
            if gameWon!=0 :
                if gameWon==1 :
                    messagebox.showinfo('TicTacToe', 'X Wins!')
                elif gameWon==2 :
                    messagebox.showinfo('TicTacToe', 'O Wins!')
            #--------------------------|announce winner|---------------------

            #print a shadow of the game board
            #----------------------------------------------------------------
            print('')
            for y in gameBox :
                for x in y :
                    if x==0 :
                        print('[ ]', end='')
                    elif x==1 :
                        print('[X]', end='')
                    elif x==2 :
                        print('[O]', end='')
                print('')
            #--------|print a shadow of the game board|----------------------

            #check if it's a tie
            #----------------------------------------------------------------
            isZero = 3
            for i in gameBox :
                if 0 not in i and gameWon==0 :
                    isZero -= 1
            if  isZero==0 :
                messagebox.showinfo('TicTacToe', 'The game is a tie')
            #--------------------|check if it's a tie|----------------------

                        #end of round menu
            #----------------------------------------------------------------
            if gameWon != 0 or isZero==0 :
                print('End of round menu start')
                whoWonTxt = StringVar()
                endMenuFrame = Frame(master)
                endMenuFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
                if gameWon==1 :
                    whoWonTxt.set('X has won this round')
                elif gameWon==0 :
                    whoWonTxt.set('O has won this round')
                elif isZero==0 :
                    whoWonTxt.set('Draw')
                else :
                    whoWonTxt.set('ERROR')
                print(whoWonTxt.get())
                whoWon = Label(endMenuFrame, textvariable=whoWonTxt, font=('Helvetica', 20))
                whoWon.grid(row=0, column=1, pady=5)

            #-----------------------|end of round menu|----------------------


        #setup the board
        #----------------------------------------------------------------
#        b1 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b1)); b1.image = img_0
#        b2 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b2)); b2.image = img_0
#        b3 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b3)); b3.image = img_0
        
#        b4 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b4)); b4.image = img_0
#        b5 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b5));# b5.image = img_0
#        b6 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b6)); b6.image = img_0

#        b7 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b7)); b7.image = img_0
#        b8 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b8)); b8.image = img_0
#        b9 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b9)); b9.image = img_0
    #-----------------------|setup the board|-------------------------------
        
        #put buttons on the grid
        #----------------------------------------------------------------
#        b1.grid(row=0, column=0, padx=(50,5), pady=(50,5)); #buttons.append(b1)
#        b2.grid(row=0, column=1, pady=(50,5)); buttons.append(b2)
#        b3.grid(row=0, column=2, padx=(5,50), pady=(50,5)); buttons.append(b3)
        
#        b4.grid(row=1, column=0, padx=(50,5)); buttons.append(b4)
#        b5.grid(row=1, column=1); #buttons.append(b5)
#        b6.grid(row=1, column=2, padx=(5,50)); buttons.append(b6)

#        b7.grid(row=2, column=0, padx=(50,5), pady=(5,50)); buttons.append(b7)
#        b8.grid(row=2, column=1, pady=(5,50)); buttons.append(b8)
#        b9.grid(row=2, column=2, padx=(5,50), pady=(5,50)); #buttons.append(b9)
        #---------------------|put buttons on the grid|-------------------

        #Compact button system
        #-----------------------------------------------------------------
        #A more compact way of making the matrix/playfeild
        compactBtn = {}
        btnRow = 3
        btnColumn = 3
        global buttons, buttonMatrix
        for i in range(btnRow*btnColumn) :
            def click_b(x=i) :
                b = compactBtn[x]
                global xTurn, count, gameWon
                if gameWon!=0 :
                    pass
                if b['image']=='pyimage1' and xTurn==True:
                    b['image']=img_1; b.image=img_1
                    xTurn=False
                    count+=1
                    gameStatus()
                elif b['image']=='pyimage1' and xTurn==False:
                    b['image']=img_2; b.image=img_2
                    xTurn=True
                    count+=1
                    gameStatus()
                else:
                    messagebox.showerror('TicTacToe', 'The box is already in use.\npick another box...')

            nameOfBtn = 'b_' + str(i+1)
            compactBtn[i] = tk.Button(master, image=img_0, relief=SUNKEN, text=nameOfBtn, command=click_b); compactBtn[i].image=img_0

        num = 0
        for x in range(1, btnRow+1) :
            buttonMatrix.append([])
            for y in range(1, btnColumn+1) :
                if x <= 1 : 
                    padyNum = [50,5]
                elif x >= btnRow :
                    padyNum = [5,50]
                else :
                    padyNum = [5,5]

                if y <= 1 : 
                    padxNum = [50,5]
                elif y >= btnColumn :
                    padxNum = [5,50]
                else :
                    padxNum = [5,5]

                buttonMatrix[x-1].append(compactBtn[num])
                compactBtn[num].grid(row=x-1, column=y-1, padx=(padxNum[0],padxNum[1]), pady=(padyNum[0],padyNum[1]))
                buttons.append(compactBtn[num])
                num+=1
        #------------------------|Compact button system|------------------
    #---------------------------------|start the game|-------------------        

#--------------------------------|the app|-----------------------

#run the app
#----------------------------------------------------------------
root = tk.Tk()
app = App(master=root)
app.mainloop()
#---------------------------------|run the app|------------------