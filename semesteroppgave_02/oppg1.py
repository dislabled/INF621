#!/usr/bin/env python3
# coding=utf-8

from csv import reader
import matplotlib.pyplot as plt

# Oppgave 1.a
def les_temp(filnavn:str, skille=',') -> dict:
    """ Henter en .csv fil og analyserer denne.

        args:
            filnavn (str): filnavn
            skille (str): symbol som skiller i csv fil

        returns:
            ordbok (dict): analyserte verdier av csv filen
    """
    ordbok = {}
    with open(filnavn, 'r') as fil:
        r = reader(fil, delimiter=skille)
        _ = next(r)     # Fjerner overskriften og plasserer den i en variabel som ikke brukes
        for linje in r:
            if linje[0] not in ordbok:
                ordbok[linje[0]] = {int(linje[1][:2]): float(linje[2])}
            else:
                ordbok[linje[0]] |= {int(linje[1][:2]): float(linje[2])} # Merk at denne bare fungerer i python v3.9
                # ordbok[linje[0]].update({linje[1] : linje[2]}) # Denne må brukes < v3.9
    return ordbok

# Oppgave 1.b
def plott(makstemp:dict) -> None:
    """ Plotter alle Maksimumstemperaturer i Norge
        i perioden 1.-30.april 2021

        args:
            makstemp (dict): ordbok med by, dato og temp
    """
    for by in makstemp:
        (y, x) = ([], [])
        for tid in sorted(makstemp[by]):
            x.append(int(tid))
            y.append(makstemp[by][tid])
        plt.plot(x, y, label=by )

    plt.title('Maksimumstemperaturer i Norge i perioden 1.-30.april 2021')
    plt.ylabel('Temperatur')
    plt.xlabel('Dato')
    plt.legend()
    plt.show()


# Oppgave 1.c
def stolper_snitt(makstemp:dict) -> None:
    """ Lager et stolpediagram over gjennomsnittlig Maksimumstemperatur
        i april for alle byene

        args:
            makstemp (dict): ordbok med by, dato og temp
    """
    gjennomsnitt = []
    for by in makstemp:
        gjennomsnitt.append(sum(list(makstemp[by].values())) / len(makstemp[by]))
    plt.title('Gjennomsnittlig makstemperatur i Norge i april 2021')
    plt.bar(makstemp.keys(), gjennomsnitt)
    plt.show()

# Oppgave 1.d
def kake(makstemp:dict) -> None:
    """ Lager et sektordiagram over hvor ofte hver by er den med høyest temperatur.

        args:
            makstemp (dict): ordbok med by, dato og temp
    """
    topp_by = [0]*len(makstemp)
    for i in range(1, 31):
        shortlist = []
        for by in makstemp.values():
            shortlist.append(by[i])
        for j, temp in enumerate(shortlist):
            if temp == max(shortlist):
                topp_by[j] +=1

    plt.title('Hvor ofte byene har høyest temperatur i april 2021.')
    plt.pie(topp_by, labels=list(makstemp), autopct='%.1f%%')
    plt.legend()
    plt.show()

if __name__ == "__main__":
# Oppgave 1.a
    ordbok = les_temp('april.csv')
# Oppgave 1.b
    plott(ordbok)
# Oppgave 1.c
    stolper_snitt(ordbok)
# Oppgave 1.d
    kake(ordbok)
