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

#Failis leheküljed.txt esimesel positsioonil on profiili nimi ja teine kuni lõpmatus positsioonil
# erinevad leheküljed
#
#Funktsioon runni() võtab failist leheküljed.txt ja pärast lehekülgede avamist programm sulgub
##def runni(event):
##	global profiil
##	valitud_profiil = profiil.get()
##	with open('leheküljed.txt') as f:
##		for rida in f:
##			#rida = rida.split(',')
##			profiilinimi = rida.split(",")[0]
##			leheküljed = rida[1]
##			if profiilinimi == valitud_profiil:
##				valitud_lehed = []
##				leheküljed = leheküljed.split(',')
##				print(leheküljed)
##				for i in leheküljed:
##                                    webbrowser.open(leheküljed)
##				break
##	window.destroy()
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

loo_uus = Button(text="Loo uus profiil", command = uus_profiil())
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