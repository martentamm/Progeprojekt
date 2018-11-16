import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.messagebox

global window
window = Tk()
window.title("Profile maker")
window.geometry('450x200')
window.iconbitmap('ikoon.ico')

def lisa_uus():
	uus_profiil = []
	a = []

	def lisa():
		a.append(lehekülje_kast.get())
		print(a)
		return a


	def lõpeta():
		f = open('leheküljed.txt')
		f.write(uus_profiil)
		f.close()
		uus_aken.destroy()
		pass

	def kustuta():
		pass

	uus_aken = Tk()
	uus_aken.title('Loo uus profiil')
	uus_aken.iconbitmap('ikoon.ico')
	uus_aken.geometry('400x400')
	profiili_nimi_label = Label(uus_aken, text="Uue profiili nimi:")
	profiili_nimi_label.place(x=10, y=20)
	profiili_nime_kast = Entry(uus_aken)
	profiili_nime_kast.place(x=110, y=20)
	lehekülje_label = Label(uus_aken, text="Lehekülje aadress:")
	lehekülje_label.place(x=10, y=40)
	lehekülje_kast = Entry(uus_aken)
	lehekülje_kast.place(x=110, y= 40)
	lisatud_leheküljed = lehekülje_kast.get()
	box = Listbox(uus_aken)

	for i in lisa():
		box.insert(END, i)

	box.config(relief=SUNKEN, border=2)
	box.place(x=200, y=200)
	lisa = Button(uus_aken, text="Lisa", command=lisa)
	lisa.place(x=300, y=10)
	lisa.config(width = 10)
	kustuta = Button(uus_aken, text="kustuta", command=kustuta)
	kustuta.place(x=300, y=40)
	kustuta.config(width=10)
	lõpeta = Button(uus_aken, text="Lõpeta", command=lõpeta)
	lõpeta.place(x=300, y=70)
	lõpeta.config(width=10)
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
                
			    
					
#Funktsioon uus_profiil() loob
def uus_profiil():
	pass


#Funktsioon profiilist() võtab failist "leheküljed.txt" kõik profiilid ja paneb need järjendisse
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

loo_uus = Button(text="Loo uus profiil", command =lisa_uus())
loo_uus.place(x=300, y=110)

pealkiri = Label(text = "Vali profiil:")
pealkiri.place(x=10, y=10)

profiil = Combobox(textvariable = nimi, values=profiililist())
profiil.SelectedIndex = -1
#profiil.bind("<<ComboboxSelected>>",runni)
#comboBox.Items.Insert(0, "Palun vali profiil")
#comboBox1.Text = "Please, select any value"
profiil.place(x=10, y=40)



window.mainloop()