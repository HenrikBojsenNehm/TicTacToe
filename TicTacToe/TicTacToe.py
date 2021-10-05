import tkinter as tk
import time

from tkinter import *
from PIL import ImageTk, Image

#Clear all widgets
def clearScreen(master):
    for widgets in master.winfo_children():
        widgets.destroy()

#button clicked function
def b_click(b):
    pass


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.startUp()

    #start up scrren
    def startUp(self):
        selfMaster = self.master
        selfMaster.title('Tic-tac-toe')
    #    selfMaster.geometry('600x400')
        selfMaster.testLabel = Label(text='Hi', font=('Helvetica', 15))
        selfMaster.testLabel.grid(row=0, column=0)
        time.sleep(2)
        self.startGame(True, selfMaster)
    
    #start the game
    def startGame(self, solo, master):
        print('Started!')
        clearScreen(master)
        
        if(solo==True):
            print('Are you okay?')
        else:
            print('Ok!')

        imageOpen_0 = Image.open('noneSelfMade.png')
        image_0 = imageOpen_0.resize((175,175), Image.ANTIALIAS)
        img_0 = ImageTk.PhotoImage(image_0)
        
        imageOpen_1 = Image.open('xSelfMade.png')
        image_1 = imageOpen_1.resize((175,175), Image.ANTIALIAS)
        img_1 = ImageTk.PhotoImage(image_1)
        
        imageOpen_2 = Image.open('oSelfMade.png')
        image_2 = imageOpen_2.resize((175,175), Image.ANTIALIAS)
        img_2 = ImageTk.PhotoImage(image_2)

        #setup the board
        b1 = Button(master, image=img_1, relief=SUNKEN, command=lambda: b_click(b1)); b1.image = img_1
        b2 = Button(master, image=img_2, relief=SUNKEN, command=lambda: b_click(b2)); b2.image = img_2
        b3 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b3)); b3.image = img_0
        
        b4 = Button(master, image=img_2, relief=SUNKEN, command=lambda: b_click(b4)); b4.image = img_2
        b5 = Button(master, image=img_1, relief=SUNKEN, command=lambda: b_click(b5)); b5.image = img_1
        b6 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b6)); b6.image = img_0

        b7 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b7)); b7.image = img_0
        b8 = Button(master, image=img_0, relief=SUNKEN, command=lambda: b_click(b8)); b8.image = img_0
        b9 = Button(master, image=img_1, relief=SUNKEN, command=lambda: b_click(b9)); b9.image = img_1

        #put buttons on the grid
        b1.grid(row=0, column=0, padx=(50,5), pady=(50,5))
        b2.grid(row=0, column=1, pady=(50,5))
        b3.grid(row=0, column=2, padx=(5,50), pady=(50,5))
        
        b4.grid(row=1, column=0, padx=(50,5))
        b5.grid(row=1, column=1)
        b6.grid(row=1, column=2, padx=(5,50))

        b7.grid(row=2, column=0, padx=(50,5), pady=(5,50))
        b8.grid(row=2, column=1, pady=(5,50))
        b9.grid(row=2, column=2, padx=(5,50), pady=(5,50))


        



root = tk.Tk()
app = App(master=root)
app.mainloop()