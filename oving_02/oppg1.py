#!/usr/bin/env python3
# coding=utf-8

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, '')

# Oppgave 1.a
def hva_er_klokken():
    """ Printer tid av et definert tidspunkt """
    tidspunkt = datetime(2021,11,4,15,59,55)
    print("Klokken er {}:{}".format(tidspunkt.hour, tidspunkt.minute))

# Oppgave 1.b
def ukedag():
    """ Skriver ut hvilken dag det er av et definert tidspunkt """
    tidspunkt = datetime(2021,11,4,15,59,55)
    print("Det er {}!".format(tidspunkt.strftime("%B")))

# Oppgave 1.c
def tidspunkt():
    """ Skriver ut dato og tid av et definert tidspunkt """
    tidspunkt = datetime(2021,11,4,15,59,55)
    print(datetime.strftime(tidspunkt, "Det er %A %-d. %B og klokken er %H:%M:%S"))

if __name__ == "__main__":
    hva_er_klokken()
    ukedag()
    tidspunkt()
