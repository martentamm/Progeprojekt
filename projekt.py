import webbrowser
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("Profile maker")
window.geometry('400x200')
window.iconbitmap('ikoon.ico')


# Failis leheküljed.txt esimesel positsioonil on profiili nimi ja teine kuni lõpmatus positsioonil
# erinevad leheküljed


# Funktsioon runni() võtab failist leheküljed.txt ja pärast lehekülgede avamist programm sulgub
def runni():
	i = 1
	with open('leheküljed.txt') as f:
		for rida in f:
			if rida.split(",")[0] == vali():
				while i < len(rida.split(",")):
					webbrowser.open_new_tab(rida.split(",")[i])
					i += 1
	window.destroy()


# Funktsioon quit() vastab nupule "Sulge"
def quit():
	window.destroy()


# Funktsioon uus_profiil() loob
##def uus_profiil():


def profiililist():
	profiilid = []
	with open('leheküljed.txt', encoding='UTF-8') as f:
		for tegevus in f:
			tegevus = tegevus.split(',')
			profiilid.append(tegevus[0].strip())
	return profiilid


def vali():
	return profiil.get()


kaivita = Button(text="käivita", command=runni)
kaivita.place(x=300, y=80)

sulge = Button(text="sulge", command=quit)
sulge.place(x=300, y=140)

profiil = Combobox(window, values=(profiililist()))
profiil.current(0)
profiil.place(x=10, y=40)

# selle nupuga saan  kasutaja poolt valitud tegevuse
value = Button(text="Vali", command=vali)
value.place(x=10, y=70)

##loo_uus = Button(text="Loo uus profiil", command = uus_profiil())
##loo_uus.place(x=300, y=110)

pealkiri = Label(window, text="Vali profiil:")
pealkiri.place(x=10, y=10)

window.mainloop()