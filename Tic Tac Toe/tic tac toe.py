from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import *

root = Tk()
root.title("Tic Tac Toe: player 1")

style = ttk.Style()
style.theme_use('classic')

# global variables
active_player = 1
p1 = [] # what player one selected
p2 = [] # what player two selected

# add Buttons
b1 =ttk.Button(root, text = ' ')
b1.grid(row = 0, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
b1.config(command = lambda: buttonclick(1))

b2 = ttk.Button(root, text = ' ')
b2.grid(row = 0, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
b2.config(command = lambda: buttonclick(2))

b3 = ttk.Button(root, text = ' ')
b3.grid(row = 0, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
b3.config(command = lambda: buttonclick(3))

b4 = ttk.Button(root, text = ' ')
b4.grid(row = 1, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
b4.config(command = lambda: buttonclick(4))

b5 = ttk.Button(root, text = ' ')
b5.grid(row = 1, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
b5.config(command = lambda: buttonclick(5))

b6 = ttk.Button(root, text = ' ')
b6.grid(row = 1, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
b6.config(command = lambda: buttonclick(6))

b7 = ttk.Button(root, text = ' ')
b7.grid(row = 2, column = 0, sticky = 'snew', ipadx = 40, ipady = 40)
b7.config(command = lambda: buttonclick(7))

b8 = ttk.Button(root, text = ' ')
b8.grid(row = 2, column = 1, sticky = 'snew', ipadx = 40, ipady = 40)
b8.config(command = lambda: buttonclick(8))

b9 = ttk.Button(root, text = ' ')
b9.grid(row = 2, column = 2, sticky = 'snew', ipadx = 40, ipady = 40)
b9.config(command = lambda: buttonclick(9))

def buttonclick(id):
	global active_player
	global p1
	global p2
	if (active_player == 1):
		setlayout(id, "X")
		p1.append(id) 
		root.title("Tic Tac Toe: player 2")
		active_player = 2
		print("P1: {}".format(p1))
		
	elif(active_player == 2):
		setlayout(id, "O")
		p2.append(id)
		root.title("Tic Tac Toe: player 1")
		active_player = 1
		print("P2: {}".format(p2))
	checkwinner()

def setlayout(id, playersymbol):
	if id == 1:
		b1.config(text = playersymbol, state = DISABLED)
	elif id == 2:
		b2.config(text = playersymbol, state=DISABLED)
	elif id == 3:
		b3.config(text = playersymbol, state=DISABLED)
	elif id == 4:
		b4.config(text = playersymbol, state=DISABLED)
	elif id == 5:
		b5.config(text = playersymbol, state=DISABLED)
	elif id == 6:
		b6.config(text = playersymbol, state=DISABLED)
	elif id == 7:
		b7.config(text = playersymbol, state=DISABLED)
	elif id == 8:
		b8.config(text = playersymbol, state=DISABLED)
	elif id == 9:
		b9.config(text = playersymbol, state=DISABLED)
		

def checkwinner():
	winner = -1
	if ((1 in p1) and (2 in p1) and (3 in p1)):
		winner = 1
	if ((1 in p2) and (2 in p2) and (3 in p2)):
		winner = 2


	if ((4 in p1) and (5 in p1) and (6 in p1)):
		winner = 1
	if ((4 in p2) and (5 in p2) and (6 in p2)):
		winner = 2


	if ((7 in p1) and (8 in p1) and (9 in p1)):
		winner = 1
	if ((7 in p2) and (8 in p2) and (9 in p2)):
		winner = 2


	if ((1 in p1) and (4 in p1) and (7 in p1)):
		winner = 1
	if ((1 in p2) and (4 in p2) and (7 in p2)):
		winner = 2


	if ((2 in p1) and (5 in p1) and (8 in p1)):
		winner = 1
	if ((2 in p2) and (5 in p2) and (8 in p2)):
		winner = 2


	if ((3 in p1) and (6 in p1) and (9 in p1)):
		winner = 1
	if ((3 in p2) and (6 in p2) and (9 in p2)):
		winner = 2


	if ((1 in p1) and (5 in p1) and (9 in p1)):
		winner = 1
	if ((1 in p2) and (5 in p2) and (9 in p2)):
		winner = 2

	if ((3 in p1) and (5 in p1) and (7 in p1)):
		winner = 1
	if ((3 in p2) and (5 in p2) and (7 in p2)):
		winner = 2


	if winner == 1:
		re = messagebox.showinfo(title = "congratulations", message = "player 1 is the winner")
		if re == 'ok':
			root.quit()
	if winner == 2:
		re = messagebox.showinfo(title = "congratulations", message = "player 2 is the winner")
		if re == 'ok':
			root.quit()




	
 
root. mainloop()