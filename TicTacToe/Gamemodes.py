from math import gamma
import tkinter as tk
from tkinter import *
from tkinter import messagebox

xTurn = bool
count = 0
gameWon = 0
buttons = []
buttonMatrix = []

class TicTacToe:
    print('Tic Tac Toe')

    def run(self, master, assets):
        global xTurn, count, buttons, gameWon

        xTurn = True
        count = 0
        gameWon = 0
        buttons =[]

        #check if win
        #----------------------------------------------------------------
        def gameStatus() :
            gameBox = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            global buttonMatrix, gameWon

            for button in buttons :
                y = button.grid_info()['row']-1
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
                #--------------------|check if it's a tie|----------------------

            self.endOfRoundMenu(gameWon, isZero, master)

        #-------------------------------|check if win|-------------------
    
        #Compact button system
        #-----------------------------------------------------------------
        #A more compact way of making the matrix/playfeild
        compactBtn = {}
        btnRow = 3
        btnColumn = 3
        global buttonMatrix

        for i in range(btnRow*btnColumn) :
            def click_b(x=i) :
                b = compactBtn[x]
                global xTurn, count

                print(f'xTurn: {xTurn} count: {count} gameWon: {gameWon}')

                if gameWon!=0 :
                    messagebox.showinfo('TicTacToe', 'You have already lost.')
                    pass
                else:
                    if b['image']=='pyimage1' and xTurn==True:
                        b['image']=assets[1]; b.image=assets[1]
                        xTurn=False
                        count+=1
                        gameStatus()
                    elif b['image']=='pyimage1' and xTurn==False:
                        b['image']=assets[2]; b.image=assets[2]
                        xTurn=True
                        count+=1
                        gameStatus()
                    else:
                        messagebox.showerror('TicTacToe', 'The box is already in use.\npick another box...')

            nameOfBtn = 'b_' + str(i+1)
            compactBtn[i] = tk.Button(master, image=assets[0], relief=SUNKEN, text=nameOfBtn, command=click_b); compactBtn[i].image=assets[0]

        num = 0
        for x in range(1, btnRow+1) :
            buttonMatrix.append([])
            for y in range(1, btnColumn+1) :
                if x <= 1 : 
                    padyNum = [15,5]
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
                compactBtn[num].grid(row=x, column=y-1, padx=(padxNum[0],padxNum[1]), pady=(padyNum[0],padyNum[1]))
                buttons.append(compactBtn[num])
                num+=1
        #------------------------|Compact button system|------------------


class UltimateTicTacToe:
    print('Ultimate Tic Tac Toe')
    
    def run(self, master, assets):
        messagebox.showinfo('TicTacToe', 'Work in progress')