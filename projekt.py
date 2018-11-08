import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.messagebox


window = Tk()
window.title("Profile maker")
window.geometry('500x200')
window.iconbitmap('ikoon.ico')

def runni():
	with open('leheküljed.txt') as f:
		for lehekulg in f:
			webbrowser.open_new_tab(lehekulg)
	window.destroy()

def quit():
	window.destroy()

def profiililist():
	pass

kaivita = Button(text="käivita", command = runni)
kaivita.place(x=400, y=125)

sulge = Button(text="sulge", command = exit)
sulge.place(x=400, y=150)

profiil = Combobox(text='profiil1',values=('uks', 'kaks'))
profiil.place(x=10, y=10)
window.mainloop()
