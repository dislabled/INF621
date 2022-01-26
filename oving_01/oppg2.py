#!/usr/bin/env python3
# coding=utf-8

from random import randint

# Oppgave 2.a
def les_ny_vare():
    vareordbok = {}
    vareordbok["navn"] = input("Navn på vare: ")
    vareordbok["pris"] = int(input("Pris på vare: "))
    vareordbok["kategori"] = input("Kategori: ")
    return vareordbok

# Oppgave 2.b
def les_utvalg():
    vareliste = []
    while True:
        if input("Vil du legge til en ny vare (j/n)?") != 'j':
            break
        vareliste.append(les_ny_vare())
    return vareliste

# Oppgave 2.c
def tell_varer(vareliste):
    for varer in vareliste:
        varer['antall'] = randint(0, 3)
    return vareliste

# Oppgave 2.d
def sett_ned_pris(vareliste, kategori, prosent):
    for varer in vareliste:
        if kategori in varer['kategori']:
            varer['pris'] = varer['pris'] - varer['pris'] * prosent / 100
    return vareliste

# Oppgave 2.e
def selg_vare(varenavn, vareliste):
    for varer in vareliste:
        if varenavn in varer['navn'] and varer['antall'] > 0:
            varer['antall'] = 0
            return varer['pris']
    return -1

# Oppgave 2.f
def selg_varer(handleliste, vareliste):
    total = 0
    for vare in handleliste:
        pris = selg_vare(vare, vareliste)
        if pris != -1:
            total += pris
    return total

if __name__ == "__main__":
    vareliste = les_utvalg()
    tell_varer(vareliste)
    sett_ned_pris(vareliste, 'frukt', 10)
    selg_vare('eple',vareliste)
    selg_vare('kål',vareliste)
    selg_varer(['eple', 'kål', 'drue', 'eple'], vareliste)
    print(vareliste)
