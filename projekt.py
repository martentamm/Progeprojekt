import webbrowser
from tkinter import *
from tkinter.ttk import *

global window
window = Tk()
window.title("Profile maker")
window.geometry('450x200')
window.iconbitmap('ikoon.ico')

def lisa_uus():

	uus_aken = Tk()
	uus_aken.title('Loo uus profiil')
	uus_aken.iconbitmap('ikoon.ico')
	uus_aken.geometry('400x400')

	tuhi = []
	def lisa():
		lehekulg = lehekülje_kast.get()

		box.insert(END, lehekulg)
		first = 0
		tuhi.append(box.get(first,END))
		print(tuhi)

	def lõpeta():
		lehekuljed = []
		profiilinimi = profiili_nime_kast.get()
		with open('leheküljed.txt', 'a') as lehekuljedtxt:
			box.get(first,last=None)
			print(box.get(first,last=None))
			uus_aken.destroy()


	def kustuta():
		box.delete(box.curselection(), box.curselection())

	profiili_nimi_label = Label(uus_aken, text="Uue profiili nimi:")
	profiili_nimi_label.place(x=10, y=20)
	profiili_nime_kast = Entry(uus_aken)
	profiili_nime_kast.place(x=110, y=20)

	lehekülje_label = Label(uus_aken, text="Lehekülje aadress:")
	lehekülje_label.place(x=10, y=40)
	lehekülje_kast = Entry(uus_aken)
	lehekülje_kast.place(x=110, y= 40)

	box = Listbox(uus_aken)
	box.config(relief=SUNKEN, border=2, width= 63)
	box.place(x=10, y=200)

	lisa = Button(uus_aken, text="Lisa", command= lisa)
	lisa.place(x=300, y=10)
	lisa.config(width = 10)

	kustuta = Button(uus_aken, text="Kustuta", command= kustuta)
	kustuta.place(x=300, y=40)
	kustuta.config(width=10)

	lõpeta = Button(uus_aken, text="Lõpeta", command= lõpeta)
	lõpeta.place(x=300, y=70)
	lõpeta.config(width=10)

	for rida in uus_profiil:
		box.insert(rida)

	uus_aken.mainloop()


def runni():
	i = 1
	with open('leheküljed.txt') as f:
		for rida in f:
			if rida.split(",")[0] == profiil.get():
				while i < len(rida.split(",")):
					webbrowser.open_new_tab(rida.split(",")[i])
					i += 1
				if i == len(rida.split(",")):
					window.close()

def profiililist():
	profiilid = []
	with open('leheküljed.txt', encoding='UTF-8') as f:
		for rida in f:
			rida = rida.split(',')
			profiilid.append(rida[0].strip())
	return profiilid


nimi = StringVar()
kaivita = Button(text="käivita", command = runni)
kaivita.place(x=300, y=80)

sulge = Button(text="sulge", command = exit)
sulge.place(x=300, y=140)

loo_uus = Button(text="Loo uus profiil", command =lisa_uus)
loo_uus.place(x=300, y=110)

pealkiri = Label(text = "Vali profiil:")
pealkiri.place(x=10, y=10)

profiil = Combobox(textvariable = nimi, values=profiililist())
profiil.SelectedIndex = -1
profiil.place(x=10, y=40)


window.mainloop()