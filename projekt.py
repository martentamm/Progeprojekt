import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter


#Tkinterile luuakse raam

global window
window = tkinter.Tk()
window.title("Profile maker")
##window.geometry('450x200')
window.iconbitmap('ikoon.ico')

#Nuppudele luuakse stiil

style = ttk.Style()
style.map("C.TButton", foreground=[('pressed' , 'white'),('active', 'blue')], background=[('pressed', '!disabled', 'blue')])


#Uue profiili lisamine

def lisa_uus():
    uus_aken = Tk()
    uus_aken.title('Loo uus profiil')
    uus_aken.iconbitmap('ikoon.ico')
    uus_aken.geometry('600x400')
    
    tuhi = []
    def lisa():
        lehekulg = lehekylje_kast.get()
        box.insert(END, lehekulg)
        
    def lopeta():
        profiilinimi = profiili_nime_kast.get()
        lehed = box.get(first=0, last=None)
        fail = open('lehekyljed.txt', "a+")
        fail.write("\n"+profiilinimi+","+lehed)
        fail.close()
        uus_aken.destroy()
    
    
    def kustuta():
        box.delete(box.curselection(), box.curselection())
    
    
    profiili_nimi_label = Label(uus_aken, text="Uue profiili nimi:", foreground="blue")
    profiili_nimi_label.place(x=10, y=20)
    profiili_nime_kast = Entry(uus_aken)
    profiili_nime_kast.place(x=130, y=20)
    
    lehekylje_label = Label(uus_aken, text="Lehekülje aadress:", foreground="blue")
    lehekylje_label.place(x=10, y=45)
    lehekylje_kast = Entry(uus_aken)
    lehekylje_kast.place(x=130, y= 45)
    
    box = Listbox(uus_aken)
    box.config(relief=SUNKEN, border=2, width= 63)
    box.place(x=10, y=200)
    
    
    lisa = ttk.Button(uus_aken, text="Lisa", style="C.TButton", command= lisa)
    lisa.place(x=330, y=10)
    lisa.config(width = 10)
    
    kustuta = Button(uus_aken, text="Kustuta", style="C.TButton", command= kustuta)
    kustuta.place(x=330, y=40)
    kustuta.config(width=10)
    
    lopeta = Button(uus_aken, text="Lõpeta", style="C.TButton", command= lopeta)
    lopeta.place(x=330, y=70)
    lopeta.config(width=10)

##	for rida in uus_profiil:
##		box.insert(rida)
    uus_aken.mainloop()


#Funktsioon avab valitud profiili alla salvestatud veebilehed
	
def runni():
    i = 1
    with open('lehekyljed.txt') as f:
        for rida in f:
            if rida.split(",")[0] == profiil.get():
                while i < len(rida.split(",")):
                    webbrowser.open_new_tab(rida.split(",")[i])
                    i += 1
                if i == len(rida.split(",")):
                    window.close()


#Funktsioon tekitab faili salvestatud profiilidest järjendi
					
def profiililist():
    profiilid = []
    with open('lehekyljed.txt', encoding='UTF-8') as f:
        for rida in f:
            rida = rida.split(',')
            profiilid.append(rida[0].strip())
    return profiilid


nimi = StringVar()
kaivita = ttk.Button(text="käivita", style = "C.TButton",command = runni)
kaivita.grid(column=4, row= 4, padx=5, pady=5)

sulge = ttk.Button(text="sulge", style="C.TButton", command = exit)
sulge.grid(column=4, row=6, padx=5, pady=5)

loo_uus = ttk.Button(text="Loo uus profiil", style="C.TButton", command= lisa_uus)
loo_uus.grid(column=4, row=2, padx=5, pady=5)

pealkiri = ttk.Label(window, text = "Vali profiil:", foreground="blue")
pealkiri.grid(column= 0 , row= 0, padx=10, pady=10, sticky=(W))

profiil = ttk.Combobox(textvariable = nimi, values=profiililist())
profiil.SelectedIndex = -1
profiil.grid(column=0, row=1, padx=5, pady=5)

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.mainloop()