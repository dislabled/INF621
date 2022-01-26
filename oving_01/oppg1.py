#!/usr/bin/env python
# coding=utf-8

# Oppgave 1.a
def erstatt(tekst, ordbok):
    nystreng = ''
    for ord in tekst.split():
        if ord in ordbok:
            nystreng += ordbok[ord] + ' '
        else:
            nystreng += ord + ' '
    return nystreng[:-1:]

# Oppgave 1.b
def les_oppgave():
    ordbok = {}
    while True:
        ord = input("Gi meg det neste ordet: (avslutt med tom streng)")
        if ord == "":
            break
        elif ord in ordbok:
            print("Tidligere ville du erstatte {} med {}".format(ord, ordbok[ord]))
        erstatning = input("Hva skal {} erstattes med: ".format(ord))
        ordbok[ord] = erstatning
    return ordbok

# Oppgave 1.c
def oversett():
    ordbok = les_oppgave()
    tekst = input("Skriv en tekst som vi skal oversette (avslutt med tom streng): ")
    if tekst != '':
        print("Den nye teksten er: {}".format(erstatt(tekst, ordbok)))


if __name__ == "__main__":
    oversett()

