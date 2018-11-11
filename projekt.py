import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.messagebox

window = Tk()
window.title("Profile maker")
window.geometry('400x200')
window.iconbitmap('ikoon.ico')

#Failis leheküljed.txt esimesel positsioonil on profiili nimi ja teine kuni lõpmatus positsioonil
# erinevad leheküljed
#
#

#Funktsioon runni() võtab failist leheküljed.txt ja pärast lehekülgede avamist programm sulgub
def runni():
	with open('leheküljed.txt') as f:
		for lehekulg in f:
			lehekulg = lehekulg.split(' ')
			webbrowser.open_new_tab(lehekulg[1])
	window.destroy()

#Funktsioon quit() vastab nupule "Sulge"
def quit():
	window.destroy()

#Funktsioon uus_profiil() loob
def uus_profiil():


kaivita = Button(text="käivita", command = runni)
kaivita.place(x=300, y=80)


def profiililist():
	profiilid = []
	with open('leheküljed.txt') as f:
		for profiil in f:
			profiil = profiil.split(' ')
			profiilid.append(profiil[0])
	return profiilid

sulge = Button(text="sulge", command = exit)
sulge.place(x=300, y=140)

loo_uus = Button(text="Loo uus profiil", command = uus_profiil())
loo_uus.place(x=300, y=110)

pealkiri = Label(window, text = "Vali profiil:")
pealkiri.place(x=10, y=10)

profiil = Combobox(values=(profiililist()))
profiil.current(0)
profiil.place(x=10, y=40)


window.mainloop()