#!/usr/bin/env python3
# coding=utf-8

import tkinter as tk
from oppg1 import lesjson
from oppg3 import kurve

smitte = lesjson('smitte.json')
mutasjoner = smitte.keys()
def plott() -> None:
    """ Lager en liste ut av alle valgte mutasjoner,
        og sender dette til funksjonen kurve for plotting
    """
    mut_plott = []
    for i in gui_liste.curselection():
        mut_plott.append(gui_liste.get(i))
    kurve(smitte, mut_plott)

vindu = tk.Tk()
vindu.bind("q", lambda _: vindu.destroy())
vindu.minsize(200, 100)
vindu.title('Plott Mutasjoner')
ramme = tk.Frame(vindu)
ramme.pack()
gui_liste = tk.Listbox(ramme, height=6, selectmode=tk.MULTIPLE)
for navn in mutasjoner:
    gui_liste.insert(tk.END, navn)
gui_liste.pack()
knapp = tk.Button(ramme, text='Plott!', command=plott)
knapp.pack()
vindu.mainloop()
