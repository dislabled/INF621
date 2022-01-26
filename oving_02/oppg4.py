#!/usr/bin/env python3
# coding=utf-8

from datetime import datetime, timedelta
from random import randint

# Oppgave 4.a
def simuler(målinger, sted, tid, t_min, t_max):
    """
    Legger til en tilfeldig generert temperatur i definert ordbok.

    Parameters:
        målinger (dict) - Ordboken som skal brukes
        sted (string)   - Stedsnavn som skal i key
        tid (datetime obj) - Tid som skal i key
        t_min           - laveste temperatur som genereres
        t_max           - høyeste temperatur som genereres
    """
    målinger[(sted, tid)] = randint(t_min, t_max)

def simuler_mange(målinger, sim_info):
    """
    Genererer en ordbok med målinger fra en liste

    Parameteres:
        målinger (dict) - Ordboken som skal brukes
        sim_info (list) - Liste med tupler med hva som skal genereres
    """
    nå = datetime.now()
    for sted, t_min, t_max, dager in sim_info:
        for i in range(dager):
            simuler(målinger, sted, nå - timedelta(days=i), t_min, t_max)

def utskrift(målinger):
    """
    Formaterer og printer ut fra ordboken (målinger)
    """
    print("{:<10}{:<22}{:>14}".format("Sted: ", "Dato: ", "Temperatur: "))
    for sted in sorted(målinger, key=målinger.get, reverse=True):
        print("{:<10}{:<22}{:>8}".format(sted[0], sted[1].strftime("%x %X"), målinger[sted]))

if __name__ == "__main__":
    målinger = {}
    sim_info = [("Bergen", 3, 14, 3),
                ("Os", 3, 12, 3),
                ("Knarvik", 5, 15, 3),
                ("Voss", 0, 10, 3)]
    simuler_mange(målinger, sim_info)
    utskrift(målinger)
