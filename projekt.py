import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.messagebox


window = Tk()
window.title("Pealkiri")
window.geometry('500x200')

def runni():
	webbrowser.open_new_tab('https://google.ee')
	webbrowser.open_new_tab('https://google.ee')
	window.destroy()

def quit():
	window.destroy()

kaivita = Button(text="käivita", command = runni)
kaivita.pack()

sulge= Button(text="sulge", command = exit)
sulge.pack()

window.mainloop()
