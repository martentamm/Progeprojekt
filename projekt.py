import webbrowser
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter


#Tkinterile luuakse raam

global window
window = tkinter.Tk()
window.title("Profile maker")
window.configure(background="#a1dbcd")
window.iconbitmap('ikoon.ico')

#Nuppudele luuakse stiil

style = ttk.Style()
style.map("C.TButton", foreground=[('pressed' , 'white'),('active', 'blue')], background=[('pressed', '!disabled', 'blue')])


#Uue profiili lisamine

def lisa_uus():
    uus_aken = Tk()
    uus_aken.title('Loo uus profiil')
    uus_aken.configure(background="#a1dbcd")
    uus_aken.iconbitmap('ikoon.ico')
    
    def lisa():
        lehekulg = lehekylje_kast.get()
        box.insert(END, lehekulg)
        lehed = box.get(first=0, last=None)
        profiilinimi = profiili_nime_kast.get()
        fail = open('lehekyljed.txt', "a+")
        for rida in fail:
            if rida.split(",")[0] == profiilinimi:
                rida.append(","+lehed)
        fail.write("\n"+profiilinimi+","+lehed)
        fail.close()
        
    def lopeta():
        uus_aken.destroy()
    
    
    def kustuta():
        box.delete(box.curselection(), box.curselection())
    
    
    profiili_nimi = ttk.Label(uus_aken, text="Uue profiili nimi:", foreground="blue")
    profiili_nimi.grid(column=1, row= 1, padx=5, pady=5, sticky=(W))
    profiili_nime_kast = ttk.Entry(uus_aken)
    profiili_nime_kast.grid(column=1, row= 2, padx=5, pady=5, sticky=(W))
    
    lehekylje_label = ttk.Label(uus_aken, text="Lehekülje aadress:", foreground="blue")
    lehekylje_label.grid(column=1, row= 3, padx=5, pady=5, sticky=(W))
    lehekylje_kast = ttk.Entry(uus_aken)
    lehekylje_kast.grid(column=1, row= 4, padx=5, pady=5, sticky=(W))
    
    box = Listbox(uus_aken)
    box.config(relief=SUNKEN, border=2, width= 50)
    box.grid(column=1, row= 5, padx=5, pady=15)
    
    lisa = ttk.Button(uus_aken, text="Lisa", command= lisa)
    lisa.grid(column=3, row= 2, padx=5, pady=5)
    
    kustuta = ttk.Button(uus_aken, text="Kustuta", command= kustuta)
    kustuta.grid(column=3, row= 3, padx=5, pady=5)
    
    lopeta = ttk.Button(uus_aken, text="Lõpeta", command= lopeta)
    lopeta.grid(column=3, row= 4, padx=5, pady=5)

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

pealkiri = ttk.Label(text = "Vali profiil:", foreground="blue")
pealkiri.grid(column= 0 , row= 1, padx=10, pady=10, sticky=(W))

profiil = ttk.Combobox(textvariable = nimi, values=profiililist())
profiil.SelectedIndex = -1
profiil.grid(column=0, row=2, padx=5, pady=5)

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.mainloop()