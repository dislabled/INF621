#!/usr/bin/env python3
# coding=utf-8

import tkinter as tk
from random import randint

def kast(_=None) -> None:
    terninger = ''
    teller.set(teller.get() + 1)
    for _ in range(5):
        terninger += str(randint(0, 6)) + ' '
    overskrift.config(text=terninger)
    knapp.config(text='Kast: {}'.format(teller.get()))

vindu = tk.Tk()
vindu.minsize(400, 200)
vindu.bind("<Escape>", lambda _: vindu.destroy())
vindu.attributes('-alpha',0.8)
vindu.title('Yatzy')
ramme = tk.Frame(vindu)
ramme.place(relx=0.5, rely=0.5, anchor='center')
overskrift = tk.Label(ramme, text='', font=('Arial', 12))
overskrift.pack()
teller = tk.IntVar(ramme, 0)
teller.set(0)
knapp = tk.Button(ramme, text='Kast: 0', command=kast)
knapp.pack()
ramme.bind('<space>', kast)
vindu.mainloop()
