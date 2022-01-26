#!/usr/bin/env python3
# coding=utf-8

import tkinter as tk

# Oppgave 1.a:
vindstyrke = {
        (0, 12):            'Lite vind',
        (12,40):            'Bris',
        (40, 76):           'Kuling',
        (76, 117):          'Storm',
        (117, 999):         'Orkan'
        }

def stringify(_=None) -> None:
    """ Sjekker om input er int, finner riktig verdi, og viser den.
    """
    if vind.get().isdigit():
        konklusjon.configure(text='Feil: Vindstyrken må være ikke negativt heltall!')
        for rekke in vindstyrke:
            if int(vind.get()) in range(rekke[0], rekke[1]):
                konklusjon.configure(text=vindstyrke[rekke])
    else:
        konklusjon.configure(text='Feil: Vindstyrken må være ikke negativt heltall!',
                foreground='red')


vindu = tk.Tk()
vindu.minsize(400, 200)
vindu.bind("<Escape>", lambda _: vindu.destroy())
vindu.attributes('-alpha',0.8)
vindu.title('Beufort')
ramme = tk.Frame(vindu)
ramme.place(relx=0.5, rely=0.5, anchor='center')
# ramme.pack(anchor='center')
overskrift = tk.Label(ramme, text='Vindstyrke (km/t):', font=('Arial', 15))
overskrift.pack()
vind = tk.StringVar(ramme, '')
lesefelt = tk.Entry(ramme, textvariable=vind, width=10)
lesefelt.pack()
knapp = tk.Button(ramme, text='OK', command=stringify)
knapp.pack()
konklusjon = tk.Label(ramme, text='')
konklusjon.pack()
lesefelt.bind('<Return>', stringify)
vindu.mainloop()
