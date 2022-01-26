#!/usr/bin/env python3
# coding=utf-8

from requests import get
import matplotlib.pyplot as plt
import tkinter as tk


# Oppgave 2.a
def stolper(funn:dict) -> None:
    """ Lager stolpediagram basert på antall funn for hvert søkeord

        args:
            funn (dict): {søkeord: {avis: 'n funn'}}
    """
    farger = ('blue', 'red', 'green', 'yellow', 'cyan', 'orange', 'pink', 'grey')
    x = 0
    tickpos = []
    avis = []
    for søkeord in funn.keys():
        avis =  list(funn[søkeord].keys())
        n_stud = len(avis)
        bredde = 1 / (n_stud + 1)
        tickpos.append((x + x + n_stud * bredde) / 2)
        farge_ind = 0
        for student in avis:
            plt.bar(x, funn[søkeord][student], width=bredde,
                    align='edge', color=farger[farge_ind])
            x += bredde
            farge_ind = (farge_ind+1) % len(farger)
        x+= bredde

    plt.xticks(tickpos, labels=funn.keys())
    plt.legend(avis)
    plt.show()


#Oppgave 2.b
def søk(søkeord:list) -> None:
    """ Bruker tilført liste med søkeord. Søker gjennom aviser og kaller på
        funksjonen stolper for presentasjon

        args:
            søkeord (list): Liste med søkeord
    """
    aviser = {
            'bt' : 'http://www.bt.no',
            'vg' : 'http://www.vg.no',
            'dagbladet' : 'http://dagbladet.no'
            }
    funn = {}

    for avis in aviser:
        r = get(aviser[avis])
        funn[avis] = {}
        for ord in søkeord:
            funn[avis] |= {ord: r.text.count(ord)}
    stolper(funn)


# Oppgave 2.c
def gui() -> None:
    """ Lager et brukergrensesnitt for å skrape aviser """

    def_søkeliste= ['Verden', 'USA', 'Europa', 'Norge', 'Noreg',
                 'Oslo', 'Bergen', 'Nyhet', 'Sport', 'Valg',
                 'Fotball', 'Klima', 'Corona', 'Korona']

    def legg_til() -> None:
        """ Legger til søkeord i søkeordslisten """
        sok = nytt_ord.get()
        if sok not in gui_liste.get(0,tk.END):
            gui_liste.insert(0, sok)

    def start_søk() -> None:
        """ Lager en liste ut av alle ord i søkefeltet,
            og sender dette til funksjonen søk
        """
        søkeliste = []
        for i in gui_liste.curselection():
            søkeliste.append(gui_liste.get(i))
        søk(søkeliste)

    # Vindu:
    vindu = tk.Tk()
    vindu.bind("<Escape>", lambda _: vindu.destroy())
    vindu.minsize(500, 400)
    vindu.title('Søkefunksjon')
    # Ramme 1:
    ramme = tk.Frame(vindu)
    ramme.grid(row=0, column=0)
    # Forklarende tekst:
    text1 = tk.Label(ramme, text='Legg til nytt søkeord:')
    text1.pack()
    # Søkeord input:
    nytt_ord = tk.StringVar(ramme, '')
    lesefelt = tk.Entry(ramme, textvariable=nytt_ord)
    lesefelt.pack()
    # Ramme 2:
    ramme2 = tk.Frame(vindu)
    ramme2.grid(row=0, column=1)
    # Knapp i ramme 1:
    knapp1 = tk.Button(ramme2, text='->', command=legg_til)
    knapp1.pack()
    # Ramme 3:
    ramme3 = tk.Frame(vindu)
    ramme3.grid(row=0, column=2)
    # Forklarende tekst:
    text2 = tk.Label(ramme3, text='Velg et eller flere søkeord: ')
    text2.pack()
    # Liste over søkeord:
    rulle = tk.Scrollbar(ramme3)
    rulle.pack(side=tk.RIGHT, fill=tk.Y)
    gui_liste = tk.Listbox(ramme3, height=15, selectmode=tk.MULTIPLE,
            yscrollcommand=rulle.set)
    for navn in def_søkeliste:
        gui_liste.insert(tk.END, navn)
    gui_liste.pack()
    rulle.config(command=gui_liste.yview)
    # Knapp i ramme 3:
    knapp2 = tk.Button(ramme3, text='Søk', command=start_søk)
    knapp2.pack()
    # Åpne vindu
    vindu.mainloop()


if __name__ == "__main__":
# Oppgave 2.a
    # funn = {}
    # funn['Norge'] = {'VG': 25, 'Dagbladet': 9, 'BT': 9}
    # funn['Bergen'] = {'VG': 10, 'Dagbladet': 0, 'BT': 47}
    # stolper(funn)
# Oppgave 2.b
    # søk(['Norge', 'Bergen', 'Nå', 'drap', 'jobb'])
# Oppgave 2.c
    gui()
