#!/usr/bin/env python3
# coding=utf-8

from datetime import datetime

# Oppgave 2.a
def parse_1(dato):
    """ 
    Tar inn en dato som 'dd.mm.yy' i en streng, og 
    returnerer som et datetime objekt
    """
    return datetime.strptime(dato, "%d.%m.%y")

# Oppgave 2.b
def parse_2(dato):
    """
    Tar inn en dato som '(d)d.navn-på-måned yyyy' i en 
    streng, og returnerer som et datetime objekt
    """
    return datetime.strptime(dato, "%d. %B %Y")

# Oppgave 2.c
def parse_3(dato):
    """
    Tar inn en dato som '(d)d/(m)m-yyyy TT:MM:SS' i en
    streng, og returnerer som et datetime objekt
    """
    return datetime.strptime(dato, "%d/%m-%Y %H:%M:%S")

if __name__ == "__main__":
    print(parse_1("04.11.21"))
    print(parse_2("4. november 2021"))
    print(parse_3("04/11-2021 15:59:55"))
