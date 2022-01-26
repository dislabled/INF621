#!/usr/bin/env python3
# coding=utf-8

from datetime import datetime
from locale import setlocale, LC_TIME

setlocale(LC_TIME, 'nb_NO.utf-8')


# Oppgave 1.a
def fil_info(filnavn):
    """
    Printer hvor mange tegn, ord og linjer i filen (filnavn)
    """
    with open(filnavn, 'r') as fil:
        ant_ord = 0
        ant_tegn = 0
        ant_linjer = 0
        for linjer in fil:
            ant_linjer += 1
            ant_ord += len(linjer.split())
            for _ in linjer.strip('\n'):
                ant_tegn += 1

    print('Det er {} tegn, {} ord og {} linjer i filen {}'.format(
            ant_tegn, ant_ord, ant_linjer, filnavn))

# Oppgave 1.b
def tidspunkt():
    """
    Lager en fil som inneholder tidspunktet når den ble opprettet
    """
    with open('nå.txt', 'w') as fil:
        nå = datetime.strftime(datetime.now(), '%A %d. %B %Y klokken %H:%M:%S.')

        fil.write('Fil opprettet {}'.format(nå))

# Oppgave 1.c
def antall(filnavn):
    """
    Lager en ordbok som inneholder nøkkel alfabetet, og returnerer denne ordboken
    med antall forekomster av bokstavene i (filnavn) som verdi
    """
    alfabetet = "abcdefghijklmnopqrstuvwxyzæøå"
    ordbok = {}
    for tegn in alfabetet:
        ordbok[tegn] = 0
    with open(filnavn, 'r') as fil:
        for linjer in fil:
            for tegn in linjer:
                if tegn.isalpha():
                    ordbok[tegn] += 1
    return ordbok


if __name__ == "__main__":
    fil_info('test.txt')
    tidspunkt()
    forekomst = antall('test.txt')
    print('Bokstaver som forekommer i filen test.txt sortert etter arvtakende forekomst:')
    for bokstav in sorted(forekomst, key=forekomst.get, reverse=True):
        f = forekomst[bokstav]
        if f>0:
            print('{}: {}'.format(bokstav, f))
