#ΚΑΛΑΚΩΝΗΣ ΓΕΩΡΓΙΟΣ
#up1083846
#Gameoflife

import tkinter as tk
import random


class Menu():
    ''' THE CLASS THAT CREATES THE GRAPHIC ELEMENTS OF THE MENU. '''

    def __init__(self, root):



        self.root = root
        self.n = 20
        self.m = 38
        self.buttonList = []
        self.board = []
        temp = []


        #CREATION OF CANVAS
        self.canvas = tk.Canvas(self.root,bg='black')
        self.canvas.pack(expand=True,fill =tk.BOTH)

        #CREATING A BUTTON GRID
        for x in range(self.n):
            for y in range(self.m):
                button = tk.Label(self.canvas, bg='black', height=2, width=4, borderwidth=2,
                               relief="ridge")
                button.grid(row=x, column=y)

                temp.append(button)
            self.buttonList.append(temp)
            temp = []
        #TITLE
        self.title()
        #GAME OF LIFE BUTTON
        self.imgb1 = tk.PhotoImage(file='playb.png')
        self.playB = tk.Button(self.canvas, bd=0, image=self.imgb1, bg='#010216', activebackground='#010216' \
                               , command=self.playButton)
        self.play = self.canvas.create_window(1002, 323, window=self.playB)
        #EXIT BUTTON
        self.imgb2 = tk.PhotoImage(file='exitb.png')
        self.exitB = tk.Button(self.canvas, bd=0, image=self.imgb2, bg='#010216', activebackground='#010216' \
                            , command=self.exitButton)
        self.exit = self.canvas.create_window(1002, 468+71, window=self.exitB)
        #HELP BUTTON
        self.imgb3 = tk.PhotoImage(file='helpb.png')
        self.helpB = tk.Button(self.canvas, bd=0, image=self.imgb3, bg='#010216', activebackground='#010216' \
                               , command=self.helpButton)
        self.help = self.canvas.create_window(1002, 396+  72, window=self.helpB)
        #LIVE FREE OR DIE BUTTON
        self.imgb4 = tk.PhotoImage(file='lfod.png')
        self.lfodB = tk.Button(self.canvas, bd=0, image=self.imgb4, bg='#010216', activebackground='#010216' \
                            , command=self.LiveFreeButton)
        self.lfod = self.canvas.create_window(1002, 396, window=self.lfodB)



    def playButton(self):
        self.canvas.destroy()
        Game(self.root)

    def LiveFreeButton(self):
        self.canvas.destroy()
        LiveFree(self.root)
    def helpButton(self):
        self.canvas.destroy()
        Help(self.root)
    def exitButton(self):
        self.root.destroy()
    def title(self):
        title = [[0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        for i in range(self.n):
            for j in range(self.m):
                try:
                    if title[i][j] == 1:
                        self.buttonList[i][j].config(bg='#FFE81F')
                except:
                    pass






class Game():
    '''THE CLASS THAT IMPLEMENTS GAME OF LIFE '''

    def __init__(self, root):
        self.root = root


        self.n=20
        self.m=30
        self.buttonList = []
        self.board = []
        self.augBoard=[]
        temp=[]
        self.NoGen=0
        self.NoCells = 0
        self.blockcntr=0
        self.beehivecntr = 0
        self.loafcntr = 0
        self.boatcntr = 0
        self.tubcntr = 0


        self.board = self.initialize(self.board)

        #CREATING CANVAS
        self.canvas = tk.Canvas(self.root, width=300, height=718, background='#2B2A4C')
        self.canvas.grid(row=0, column=1)
        #CREATING FRAME FRAME
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0, sticky="n")

        for x in range(self.n):
            for y in range(self.m):
                button = tk.Label(master=self.frame, bg='white', height=2, width=4, borderwidth=2,
                               relief="ridge")
                button.grid(row=x, column=y)
                button.bind("<Button-1>", self.click)
                
                temp.append(button)
            self.buttonList.append(temp)
            temp = []
        #GLIDER BUTTON
        gliderw = tk.Button(self.canvas, bg='#bf211e',font='Consolas',activebackground='#8b0000',width=7, text="GLIDER", command=self.glider)
        self.canvas.create_window(45,70-8, window=gliderw)
        # BLOCK BUTTON
        blockw = tk.Button(self.canvas, bg='#bf211e',font='Consolas',activebackground='#8b0000',width=7, text="BLOCK", command=self.block)
        self.canvas.create_window(129,70-8, window=blockw)
        #BEEHIVE BUTTON
        beehivew = tk.Button(self.canvas, bg='#bf211e', font='Consolas', activebackground='#8b0000', width=7, text="BEEHIVE",
                        command=self.beehive)
        self.canvas.create_window(132, 120-8, window=beehivew)

        #LIGHTWEIGHT SPACESHIP BUTTON
        lwws = tk.Button(self.canvas, bg='#bf211e',font='Consolas15',width=7,activebackground='#8b0000', text="LWWS", command=self.LWWS)
        self.canvas.create_window(215, 70-8, window=lwws)

        #BEACON BUTTON
        beaconw = tk.Button(self.canvas, bg='#bf211e',font='Consolas 15',width=7,activebackground='#8b0000', text="BEACON", command=self.beacon)
        self.canvas.create_window(45,120-8, window=beaconw)

        #TOAD BUTTON
        toadw = tk.Button(self.canvas, bg='#bf211e',font='Consolas 15',width=7,activebackground='#8b0000', text="TOAD", command=self.toad)
        self.canvas.create_window(218, 120-8, window=toadw)
        #TUB BUTTON
        tubw= tk.Button(self.canvas, bg='#bf211e', font='Consolas 15', width=7, activebackground='#8b0000', text="TUB",
                       command=self.tub)
        self.canvas.create_window(218, 120+40, window=tubw)
        #BOAT BUTTON
        boatw = tk.Button(self.canvas, bg='#bf211e', font='Consolas 15', width=7, activebackground='#8b0000', text="BOAT",
                      command=self.boat)
        self.canvas.create_window(45, 120 + 40, window=boatw)
        #LOAF BUTTON
        loafw = tk.Button(self.canvas, bg='#bf211e', font='Consolas 15', width=7, activebackground='#8b0000', text="LOAF",
                       command=self.loaf)
        self.canvas.create_window(131, 120 + 40, window=loafw)

        #GENERATION STRINGVAR
        self.genDisplay = tk.StringVar()
        label = tk.Label(self.canvas, bg='#c3c91f', font='Consolas', textvariable=self.genDisplay)
        self.genDisplay.set('GENERATION ' + str(self.NoGen))
        self.canvas.create_window(125, 14, window=label)

        #BLOCK STRINGVAR
        self.blockDisplay = tk.StringVar()
        labelb = tk.Label(self.canvas,bg='#c3c91f',font='Consolas',width=300, textvariable=self.blockDisplay)
        self.blockDisplay.set('Block: '+'{:.2f}'.format(0)+"%")
        self.canvas.create_window(125, 200, window=labelb)

        #BEEHIVE STRINGVAR
        self.beehiveDisplay = tk.StringVar()
        labelbee = tk.Label(self.canvas,bg='#c3c91f',font='Consolas',width=300, textvariable=self.beehiveDisplay)
        self.beehiveDisplay.set('Beehive: ' + '{:.2f}'.format(0)+"%")
        self.canvas.create_window(135, 220, window=labelbee)

        #LOAF STRINGVAR
        self.loafDisplay = tk.StringVar()
        labeloaf = tk.Label(self.canvas,bg='#c3c91f',font='Consolas',width=300, textvariable=self.loafDisplay)
        self.loafDisplay.set('Loaf: ' + '{:.2f}'.format(0) + "%")
        self.canvas.create_window(120, 240, window=labeloaf)

        #BOAT STRINGVAR
        self.boatDisplay = tk.StringVar()
        labelboat = tk.Label(self.canvas,bg='#c3c91f',font='Consolas',width=300, textvariable=self.boatDisplay)
        self.boatDisplay.set('Boat: ' + '{:.2f}'.format(0) + "%")
        self.canvas.create_window(120, 260, window=labelboat)

        #TUB STRINGVAR
        self.tubDisplay = tk.StringVar()
        labelt = tk.Label(self.canvas,bg='#c3c91f',font='Consolas',width=300, textvariable=self.tubDisplay)
        self.tubDisplay.set('Tub: ' + '{:.2f}'.format(0) + "%")
        self.canvas.create_window(114, 280, window=labelt)

        #SKIP GENERARION BUTTON
        label3 = tk.Button(self.canvas,bg='#bf211e',font='Consolas',activebackground='#8b0000', text="SKIP GENERATIONS",command=lambda a=1 :self.skip(a))
        self.canvas.create_window(92,450, window=label3)
        self.gen_alter = tk.Entry(self.canvas, width=5)
        self.canvas.create_window(210, 450, window=self.gen_alter)
        self.gen_alter.bind("<Return>", self.skip)

        #CLEAR BUTTON
        clear = tk.Button(self.canvas, bg='#bf211e',activebackground='#8b0000', text="CLEAR",font='Consolas', command=self.buttonClear)
        self.canvas.create_window(218, 600, window=clear)

        #RANDOMIZE BUTTON
        random = tk.Button(self.canvas, bg='#bf211e',activebackground='#8b0000', text="RANDOMIZE",font='Consolas', command=lambda event=1 :self.randomize(event))
        self.canvas.create_window(60, 500, window=random)
        self.cells = tk.Entry(self.canvas, width=5)
        self.canvas.create_window(138, 500, window=self.cells)
        self.cells.bind("<Return>", self.randomize)
        button = tk.Button(self.canvas, bg='#bf211e', font='Consolas',activebackground='#8b0000', text="NEXT",
                        command=lambda c=self.board: self.nextgen(c))
        self.canvas.create_window(40, 600, window=button)

        #BACK BUTTON
        backbutton = tk.Button(self.canvas, bg='#bf211e', font='Consolas',activebackground='#8b0000', text="BACK",
                        command=self.back)
        self.canvas.create_window(40, 700, window=backbutton)
    def back(self):
        self.canvas.destroy()
        self.frame.destroy()
        Menu(self.root)
    
    def click(self,event):
        exit = 0
        for x in range(self.n):
            if exit == 1: break
            for y in range(self.m):
                if event.widget == self.buttonList[x][y]:
                    i = x
                    j = y
                    exit = 1
        
        if event.widget['bg'] == 'white':
            event.widget.config(bg='black')
            self.board[i][j] = 1
        else:
            event.widget.config(bg='white')
            self.board[i][j] = 0
    #FUNCTION THAT CALCULATES  NEXT GENERATION'S GRID
    def nextgen(self,board):
        self.board=board

        self.NoGen+=1

        self.genDisplay.set('GENERATION '+str(self.NoGen))


        self.status = 0
        tempBoard = []

        temp = []
        for x in range(self.n):
            for y in range(self.m):
                temp.append(0)
            tempBoard.append(temp)
            temp = []


        for x in range(self.n):
            for y in range(self.m):

                tempBoard[x][y] = self.board[x][y]

        # CHECKINH NEIGHBORING CELLS
        for x in range(self.n):
            for y in range(self.m):
                self.neighborhood(x,y)



                #IMPLEMENTING CONWAY'S RULES
                if ((self.status == 2 or self.status == 3) and self.board[x][y] == 1):
                    self.buttonList[x][y].config(bg='black')
                    tempBoard[x][y] = 1


                elif (self.status == 3 and self.board[x][y] == 0):
                    self.buttonList[x][y].config(bg='black')
                    tempBoard[x][y] = 1

                else:
                    self.buttonList[x][y].config(bg='white')
                    tempBoard[x][y] = 0

                self.status = 0

        for x in range(self.n):
            for y in range(self.m):
                self.board[x][y] = tempBoard[x][y]

        #CHECKING FOR SPECIFIC LIFEFORMS
        self.check()
        total = self.blockcntr + self.beehivecntr + self.loafcntr + self.boatcntr + self.tubcntr
        if total:
            self.blockDisplay.set('Block: ' + '{:.2f}'.format(100 * (self.blockcntr) / total) + '%')
            self.beehiveDisplay.set('Beehive: ' + '{:.2f}'.format(100 * (self.beehivecntr) / total) + '%')
            self.loafDisplay.set('Loaf: ' + '{:.2f}'.format(100 * (self.loafcntr) / total) + '%')
            self.boatDisplay.set('Boat: ' + '{:.2f}'.format(100 * (self.boatcntr) / total) + '%')
            self.tubDisplay.set('Tub: ' + '{:.2f}'.format(100 * (self.tubcntr) / total) + '%')
        else:
            self.blockDisplay.set('Block: ' + '{:.2f}'.format(0) + "%")
            self.beehiveDisplay.set('Beehive: ' + '{:.2f}'.format(0) + '%')
            self.loafDisplay.set('Loaf: ' + '{:.2f}'.format(0)+ '%')
            self.boatDisplay.set('Boat: ' + '{:.2f}'.format(0) + '%')
            self.tubDisplay.set('Tub: ' + '{:.2f}'.format(0) + '%')

    def neighborhood(self,x,y):
        if (x != 0 and x != self.n - 1 and y != 0 and y != self.m - 1):
            if (self.board[x - 1][y - 1] == 1): self.status += 1
            if (self.board[x - 1][y] == 1): self.status += 1
            if (self.board[x - 1][y + 1] == 1): self.status += 1
            if (self.board[x][y - 1] == 1): self.status += 1
            if (self.board[x][y + 1] == 1): self.status += 1
            if (self.board[x + 1][y - 1] == 1): self.status += 1
            if (self.board[x + 1][y] == 1): self.status += 1
            if (self.board[x + 1][y + 1] == 1): self.status += 1

        if (x == 0 and y != self.m - 1 and y != 0):
            if (self.board[self.n - 1][y - 1] == 1): self.status += 1
            if (self.board[self.n - 1][y] == 1): self.status += 1
            if (self.board[self.n - 1][y + 1] == 1): self.status += 1
            if (self.board[x][y - 1] == 1): self.status += 1
            if (self.board[x][y + 1] == 1): self.status += 1
            if (self.board[x + 1][y - 1] == 1): self.status += 1
            if (self.board[x + 1][y] == 1): self.status += 1
            if (self.board[x + 1][y + 1] == 1): self.status += 1

        if (y == 0 and x != self.n - 1 and x != 0):
            if (self.board[x - 1][self.m - 1] == 1): self.status += 1
            if (self.board[x - 1][y] == 1): self.status += 1
            if (self.board[x - 1][y + 1] == 1): self.status += 1
            if (self.board[x][self.m - 1] == 1): self.status += 1
            if (self.board[x][y + 1] == 1): self.status += 1
            if (self.board[x + 1][self.m - 1] == 1): self.status += 1
            if (self.board[x + 1][y] == 1): self.status += 1
            if (self.board[x + 1][y + 1] == 1): self.status += 1

        if (x == self.n - 1 and y != self.m - 1 and y != 0):
            if (self.board[x - 1][y - 1] == 1): self.status += 1
            if (self.board[x - 1][y] == 1): self.status += 1
            if (self.board[x - 1][y + 1] == 1): self.status += 1
            if (self.board[x][y - 1] == 1): self.status += 1
            if (self.board[x][y + 1] == 1): self.status += 1
            if (self.board[0][y - 1] == 1): self.status += 1
            if (self.board[0][y] == 1): self.status += 1
            if (self.board[0][y + 1] == 1): self.status += 1

        if (y == self.m - 1 and x != self.n - 1 and x != 0):
            if (self.board[x - 1][y - 1] == 1): self.status += 1
            if (self.board[x - 1][y] == 1): self.status += 1
            if (self.board[x - 1][0] == 1): self.status += 1
            if (self.board[x][y - 1] == 1): self.status += 1
            if (self.board[x][0] == 1): self.status += 1
            if (self.board[x + 1][y - 1] == 1): self.status += 1
            if (self.board[x + 1][y] == 1): self.status += 1
            if (self.board[x + 1][0] == 1): self.status += 1

        if (x == 0 and y == 0):

            if (self.board[self.n - 1][self.m - 1] == 1): self.status += 1
            if (self.board[self.n - 1][y] == 1): self.status += 1
            if (self.board[self.n - 1][y + 1] == 1): self.status += 1
            if (self.board[x][self.m - 1] == 1): self.status += 1
            if (self.board[x][y + 1] == 1): self.status += 1
            if (self.board[x + 1][self.m - 1] == 1): self.status += 1
            if (self.board[x + 1][y] == 1): self.status += 1
            if (self.board[x + 1][y + 1] == 1): self.status += 1

        if (x == 0 and y == self.m - 1):

            if (self.board[self.n - 1][y - 1] == 1): self.status += 1
            if (self.board[self.n - 1][y] == 1): self.status += 1
            if (self.board[self.n - 1][0] == 1): self.status += 1
            if (self.board[x][y - 1] == 1): self.status += 1
            if (self.board[x][0] == 1): self.status += 1
            if (self.board[x + 1][y - 1] == 1): self.status += 1
            if (self.board[x + 1][y] == 1): self.status += 1
            if (self.board[x + 1][0] == 1): self.status += 1

        if (y == 0 and x == self.n - 1):

            if (self.board[x - 1][self.m - 1] == 1): self.status += 1
            if (self.board[x - 1][y] == 1): self.status += 1
            if (self.board[x - 1][y + 1] == 1): self.status += 1
            if (self.board[x][self.m - 1] == 1): self.status += 1
            if (self.board[x][y + 1] == 1): self.status += 1
            if (self.board[0][self.m - 1] == 1): self.status += 1
            if (self.board[0][y] == 1): self.status += 1
            if (self.board[0][y + 1] == 1): self.status += 1

        if (x == self.n - 1 and y == self.m - 1):

            if (self.board[x - 1][y - 1] == 1): self.status += 1
            if (self.board[x - 1][y] == 1): self.status += 1
            if (self.board[x - 1][0] == 1): self.status += 1
            if (self.board[x][y - 1] == 1): self.status += 1
            if (self.board[x][0] == 1): self.status += 1
            if (self.board[0][y - 1] == 1): self.status += 1
            if (self.board[0][y] == 1): self.status += 1
            if (self.board[0][0] == 1): self.status += 1
    def check(self):
        self.aug()
        self.blockcntr = 0
        self.beehivecntr = 0
        self.loafcntr = 0
        self.boatcntr = 0
        self.tubcntr = 0
        for i in range(self.n):
            for j in range(self.m):
                try:
                    if self.blockCheck(i,j):self.blockcntr+=1
                    if self.beehiveCheck(i, j):self.beehivecntr+=1
                    if self.loafCheck(i, j): self.loafcntr+=1
                    if self.boatCheck(i, j): self.boatcntr+=1
                    if self.tubCheck(i, j): self.tubcntr+=1

                except:pass
    def randomize(self,event):
        try:
            for i in range(int(self.cells.get())):
                x=random.randint(0,self.n-1)
                y = random.randint(0, self.m - 1)
                self.board[x][y]=1
            self.draw()

        except:pass
    def initialize(self,board):
        self.board=board
        temp = []
        for x in range(self.n):
            for y in range(self.m):
                temp.append(0)
            board.append(temp)
            temp = []
        return board

    def clear(self):

        self.NoGen=0
        self.NoCells=0
        self.blockcntr = 0
        self.beehivecntr = 0
        self.loafcntr = 0
        self.boatcntr = 0
        self.tubcntr = 0
        self.genDisplay.set('GENERATION '+str(self.NoGen))
        for x in range(self.n):
            for y in range(self.m):
                self.board[x][y] = 0
    #GLIDER IMPLEMENTATION
    def glider(self):


        self.clear()
        x = round(self.n / 2)
        y = round(self.m / 2)
        self.board [x][y] = 1
        self.board [x - 1][y] = 1
        self.board [x + 1][y] = 1
        self.board [x + 1][y - 1] = 1
        self.board [x][y - 2] = 1
        self.draw()

    #LIGHTWEIGHT SPACESHIP IMPLEMENTATION
    def LWWS(self):

        self.clear()

        x = round(self.n / 2)
        y = round(self.m / 2)
        self.board [x][y] = 1
        self.board [x + 1][y + 1] = 1
        self.board [x + 2][y + 1] = 1
        self.board [x + 3][y + 1] = 1
        self.board [x + 3][y] = 1
        self.board [x + 3][y - 1] = 1
        self.board [x + 3][y - 2] = 1
        self.board [x + 2][y - 3] = 1
        self.board [x][y - 3] = 1
        self.draw()
 
    #BEACON IMPLEMENTATION
    def beacon(self):
        self.clear()

        x = round(self.n / 2)
        y = round(self.m / 2)
        self.board[x][y] = 1
        self.board[x][y + 1] = 1
        self.board[x - 1][y] = 1
        self.board[x - 2][y + 3] = 1
        self.board[x - 3][y + 3] = 1
        self.board[x - 3][y + 2] = 1
        self.draw()

    #TOAD IMPLEMENTATION
    def toad(self):
        self.clear()

        x = round(self.n / 2)
        y = round(self.m / 2)
        self.board[x][y] = 1
        self.board[x][y + 1] = 1
        self.board[x][y + 2] = 1
        self.board[x + 1][y] = 1
        self.board[x + 1][y + 1] = 1
        self.board[x + 1][y - 1] = 1
        self.draw()
    #TUB IMPLEMENTATION
    def tub(self):
        self.clear()
        i = round(self.n / 2)
        j = round(self.m / 2)
        self.board[i][j] = 1
        self.board[i - 1][j + 1] = 1
        self.board[i][j + 2]= 1
        self.board[i + 1][j + 1] = 1
        self.draw()
    #BLOCK IMPLEMENTATION
    def block(self):
            self.clear()
            i = round(self.n / 2)
            j = round(self.m / 2)
            self.board[i][j] = 1
            self.board[i - 1][j] = 1
            self.board[i - 1][j + 1] = 1
            self.board[i][j + 1] = 1
            self.draw()

    #BOAT IMPLEMENTATION
    def boat(self):
        self.clear()
        i = round(self.n / 2)
        j = round(self.m / 2)
        self.board[i][j] = 1
        self.board[i - 1][j] = 1
        self.board[i - 1][j + 1] = 1
        self.board[i + 1][j + 1] = 1
        self.board[i][j + 2] = 1
        self.draw()

    #BEEHIVE IMPLEMENTATION
    def beehive(self):
        self.clear()
        i = round(self.n / 2)
        j = round(self.m / 2)
        self.board[i][j] = 1
        self.board[i][j] = 1
        self.board[i - 1][j + 1] = 1
        self.board[i - 1][j + 2] = 1
        self.board[i][j + 3] = 1
        self.board[i + 1][j + 1] = 1
        self.board[i + 1][j + 2] = 1
        self.draw()

    #LOAF IMPLEMENTATION
    def loaf(self):
            self.clear()
            i = round(self.n / 2)
            j = round(self.m / 2)
            self.board[i][j] = 1
            self.board[i - 1][j + 1] = 1
            self.board[i - 1][j + 2] = 1
            self.board[i][j + 3] = 1
            self.board[i + 1][j + 1] = 1
            self.board[i + 2][j + 2] = 1
            self.board[i + 1][j + 3] = 1
            self.draw()

    #CHECKING FOR  BLOCKS
    def  blockCheck(self,i,j):
        check = 0
        if self.augBoard[i][j]==1:check+=1
        if self.augBoard[i-1][j] == 1: check += 1
        if self.augBoard[i-1][j+1] == 1: check += 1
        if self.augBoard[i][j+1] == 1: check += 1

        if check==4:return 1
        else:return 0

    #CHECKING FOR  BEEHIVES
    def beehiveCheck(self, i, j):
        check = 0
        if self.augBoard[i][j] == 1: check += 1
        if self.augBoard[i - 1][j+1] == 1: check += 1
        if self.augBoard[i - 1][j + 2] == 1: check += 1
        if self.augBoard[i][j + 3] == 1: check += 1
        if self.augBoard[i + 1][j + 1] == 1: check += 1
        if self.augBoard[i + 1][j + 2] == 1: check += 1

        if check == 6:
            return 1
        else:
            return 0

    #CHECKING FOR  LOAFS 
    def loafCheck(self, i, j):
        check = 0
        if self.augBoard[i][j] == 1: check += 1
        if self.augBoard[i - 1][j+1] == 1: check += 1
        if self.augBoard[i - 1][j + 2] == 1: check += 1
        if self.augBoard[i][j + 3] == 1: check += 1
        if self.augBoard[i + 1][j + 1] == 1: check += 1
        if self.augBoard[i + 2][j + 2] == 1: check += 1
        if self.augBoard[i + 1][j + 3] == 1: check += 1

        if check == 7:
            return 1
        else:
            return 0

    #CHECKING FOR BOATS
    def boatCheck(self, i, j):
        check = 0
        if self.augBoard[i][j] == 1: check += 1
        if self.augBoard[i - 1][j] == 1: check += 1
        if self.augBoard[i - 1][j + 1] == 1: check += 1
        if self.augBoard[i + 1][j + 1] == 1: check += 1
        if self.augBoard[i][j + 2] == 1: check += 1

        if check == 5:
            return 1
        else:
            return 0

    #CHECKING FOR  TUBS
    def  tubCheck(self,i,j):
        check = 0
        if self.augBoard[i][j]==1:check+=1
        if self.augBoard[i-1][j+1] == 1: check += 1
        if self.augBoard[i][j+2] == 1: check += 1
        if self.augBoard[i+1][j+1] == 1: check += 1

        if check==4:return 1
        else:return 0

    #SAVING THE STATUS OF THE GRID
    def draw(self):

        for x in range(self.n):
            for y in range(self.m):
                if self.board[x][y] == 1:
                    self.buttonList[x][y].config(bg="black")
                else:
                    self.buttonList[x][y].config(bg="white")
    def buttonClear(self):
        self.clear()
        self.draw()

    def skip(self,event):
        try:
            gen=int(self.gen_alter.get())
            for i in range(gen):
                self.nextgen(self.board)
        except:pass
    # AUGMENTED MATRIX THAT CONSIDERS THE LEFT-RIGHT SIDES BORDER AND THE TOP-BOTTOM SIDES BORDER
    def aug(self):
        temp = []
        re = []
        self.augBoard=[]

        for x in range(self.m):
            re.append(0)
        for x in range(self.n):
            temp.append(re)
        for x in range(self.n):
            temp[x] = self.board[x][:]

        self.augBoard.append(temp[self.n - 1])
        for x in range(self.n):
            self.augBoard.append(temp[x])
        self.augBoard.append(temp[0])

        for x in range(self.n):
            self.augBoard[x + 1].insert(0, temp[x][self.m - 1])
            self.augBoard[x + 1].insert(self.n + 10, temp[x][0])



class LiveFree():
    def __init__(self, root):
        '''THE  CLASS THAT IMPLEMENTS LIVE FREE OR DIE. '''
        self.root = root

        self.n = 20
        self.m = 30
        self.buttonList = []
        self.board = []
        temp = []
        self.NoGen = 0
        self.NoCells = 0


        self.board = Game.initialize(self,self.board)

        #CREATION OF CANVAS
        self.canvas = tk.Canvas(self.root, width=300, height=718, background='#4169e1')
        self.canvas.grid(row=0, column=1)
        #CREATION OF A FRAME
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0, sticky="n")

        for x in range(self.n):
            for y in range(self.m):
                button = tk.Label(master=self.frame, bg='white', height=2, width=4, borderwidth=2,
                               relief="ridge")
                button.grid(row=x, column=y)
                button.bind("<Button-1>", lambda event=1 :Game.click(self,event))
                temp.append(button)
            self.buttonList.append(temp)
            temp = []


        #GENERATION STRINGVAR
        self.genDisplay = tk.StringVar()
        label = tk.Label(self.canvas, bg='#c3c91f', font='Consolas', textvariable=self.genDisplay)
        self.genDisplay.set('GENERATION ' + str(self.NoGen))
        self.canvas.create_window(125, 14, window=label)



        #SKIP GENERATIONS BUTTON
        label3 = tk.Button(self.canvas, bg='#bf211e', font='Consolas', activebackground='#8b0000', text="SKIP GENERATIONS",
                        command=lambda a=1: self.skip(a))
        self.canvas.create_window(92, 450, window=label3)
        self.gen_alter = tk.Entry(self.canvas, width=5)
        self.canvas.create_window(210, 450, window=self.gen_alter)
        self.gen_alter.bind("<Return>",self.skip)

        #CLEAR BUTTON
        clear = tk.Button(self.canvas, bg='#bf211e', activebackground='#8b0000', text="CLEAR", font='Consolas',
                       command=self.buttonClear)
        self.canvas.create_window(218, 600, window=clear)

        #RANDOMIZE BUTTON
        random = tk.Button(self.canvas, bg='#bf211e', activebackground='#8b0000', text="RANDOMIZE", font='Consolas',
                        command=lambda event=1:self.randomize(event))
        self.canvas.create_window(60, 500, window=random)
        self.cells = tk.Entry(self.canvas, width=5)
        self.canvas.create_window(138, 500, window=self.cells)
        self.cells.bind("<Return>", self.randomize)
        button = tk.Button(self.canvas, bg='#bf211e', font='Consolas', activebackground='#8b0000', text="NEXT",
                        command=lambda c=self.board: self.nextgen(c))
        self.canvas.create_window(40, 600, window=button)

        #BACK BUTTON
        backbutton = tk.Button(self.canvas, bg='#bf211e', font='Consolas', activebackground='#8b0000', text="BACK",
                            command=self.back)
        self.canvas.create_window(40, 700, window=backbutton)


    #FUNCTION THAT CALCULATES  NEXT GENERATION'S GRID
    def nextgen(self, board):
        self.board = board

        self.NoGen += 1

        self.genDisplay.set('GENERATION ' + str(self.NoGen))

        self.status = 0
        tempBoard = []

        temp = []
        for x in range(self.n):
            for y in range(self.m):
                temp.append(0)
            tempBoard.append(temp)
            temp = []

        for x in range(self.n):
            for y in range(self.m):
                tempBoard[x][y] = self.board[x][y]

        #CHECKING NEIGHNORING CELLS
        for x in range(self.n):
            for y in range(self.m):
                Game.neighborhood(self,x,y)

                #IMPLEMENTING THE RULES OF LIVE FREE OR DIE
                if (self.status == 0 and  self.board[x][y] == 1):
                    self.buttonList[x][y].config(bg='black')
                    tempBoard[x][y] = 1


                elif (self.status == 2 and self.board[x][y] == 0):
                    self.buttonList[x][y].config(bg='black')
                    tempBoard[x][y] = 1

                else:
                    self.buttonList[x][y].config(bg='white')
                    tempBoard[x][y] = 0

                self.status = 0

        for x in range(self.n):
            for y in range(self.m):
                self.board[x][y] = tempBoard[x][y]

    def buttonClear(self):
        Game.clear(self)
        Game.draw(self)

    def randomize(self,event):
       try:
            for i in range(int(self.cells.get())):
                x=random.randint(0,self.n-1)
                y = random.randint(0, self.m - 1)
                self.board[x][y]=1
            Game.draw(self)
       except:pass

    def back(self):
        self.canvas.destroy()
        self.frame.destroy()
        Menu(self.root)


    def skip(self,event):
        try:
            gen=int(self.gen_alter.get())
            for i in range(gen):
                self.nextgen(self.board)
        except:pass


class Help():
    '''THE CLASS THAT PRESENTS SOME HELPFULL TIPS'''
    def __init__(self, root):
        self.root = root
   
        self.canvas = tk.Canvas(self.root,bg='black')
        self.canvas.pack(expand=True,fill =tk.BOTH)

        label = tk.Label(self.canvas,bg='black',fg='#FFE81F', font='Consolas 30', text='HELP')
        self.canvas.create_window(50, 30, window=label)
        label1 = tk.Label(self.canvas, bg='black', fg='#FFE81F', font='Consolas 20', text='GAME OF LIFE')
        self.canvas.create_window(95, 80, window=label1)
        label2 = tk.Label(self.canvas, bg='black', fg='#FFE81F',justify=tk.LEFT, font='Consolas 15', text='Any live cell with two or three live neighbours survives.\n'\
        'Any dead cell with three live neighbours becomes a live cell\n'\
        'All other live cells die in the next generation\nAll other dead cells stay dead\n')
        self.canvas.create_window(340, 160, window=label2)


        label3 = tk.Label(self.canvas, bg='black', fg='#FFE81F', font='Consolas 20', text='LIVE FREE OR DIE')
        self.canvas.create_window(125, 400, window=label3)
        label4 = tk.Label(self.canvas, bg='black', fg='#FFE81F', justify=tk.LEFT, font='Consolas 15',
                       text='Any live cell with no live neighbours survives\n' \
                            'Any dead cell with two live neighbours becomes a live cell\n' \
                            'All other live cells die in the next generation\nAll other dead cells stay dead\n')

        self.canvas.create_window(330, 500, window=label4)







        #EXIT BUTTON
        self.imgb3 = tk.PhotoImage(file='exitb.png')
        self.exitB = tk.Button(self.canvas, bd=0, image=self.imgb3, bg='#010216', activebackground='#010216' \
                            , command=self.back)
        self.exit = self.canvas.create_window(1002, 600, window=self.exitB)

    def back(self):
        self.canvas.destroy()
        Menu(self.root)
if __name__ == '__main__':
     root =tk.Tk()
     #DIMENSIONS
     root.geometry('1280x718')
     root.resizable(False, False)
     #TITLE
     root.title('GAME OF LIFE')
     #ICON
     root.iconbitmap(r'icon.ico')
     m = Menu(root)
     root.mainloop()