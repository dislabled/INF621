#!/usr/bin/env python3
# coding=utf-8

from random import randint
import matplotlib.pyplot as plt

# Oppgave 1.a
def kurvediagram() -> None:
    """
    Plotter kurver av 10 terningkast som viser utviklingen av:
        gjennomsnittsverdien oppnådd med terninger så langt
        minimumsverdien oppnådd med terninger så langt
        maksimumsverdien oppnådd med terninger så langt.
    """
    sum = 0
    minimum = [6]
    maximum = [0]
    gjennomsnitt= []
    for i in range(0, 10):
        kast = randint(1, 6)
        sum += kast
        if i != 0:
            gjennomsnitt.append(sum / i)
        else:
            gjennomsnitt.append(kast)
        if kast >= maximum[-1]:
            maximum.append(kast)
        else:
            maximum.append(maximum[-1])
        if kast <= minimum[-1]:
            minimum.append(kast)
        else:
            minimum.append(minimum[-1])
    minimum.pop(0)
    maximum.pop(0)
    x = range(1, 11)
    plt.plot(x, gjennomsnitt, 'r', label='Gjennomsnitt')
    plt.plot(x, minimum, 'g', label='Minste')
    plt.plot(x, maximum, 'b', label='Største')
    plt.legend()
    plt.show()

# Oppgave 1.b
def punktdiagram() -> None:
    """
    Lager et punktdiagram av 10 kast med 2 terninger
    """
    (terning1, terning2) = ([], [])
    for _ in range(0, 10):
        terning1.append(randint(1,6))
        terning2.append(randint(1,6))
    plt.scatter(terning1, terning2)
    plt.show()

# Oppgave 1.c
def stolpediagram() -> None:
    """
    Lager et stolpediagram av hvor mange av 100 terningkast
    som ga verdiene 1 - 6
    """
    x = range(1, 7)
    y = [0, 0, 0, 0, 0, 0]
    for _ in range(0, 100):
        kast = randint(1, 6)
        y[kast - 1] += 1
    plt.bar(x, y)
    plt.show()

def dobbel_stolpediagram() -> None:
    """
    Lager et stolpediagram av hvor mange av 100 terningkast
    med 2 terninger(rød og blå) som ga verdiene 1 - 6
    """
    x = range(1, 7)
    y_blå = [0]*6
    y_rød = [0]*6
    for _ in range(0, 100):
        blå_kast = randint(1, 6)
        rød_kast = randint(1, 6)
        y_blå[blå_kast - 1] += 1
        y_rød[rød_kast - 1] += 1
    plt.bar(x, y_blå, width=-0.4, align='edge', color='blue')
    plt.bar(x, y_rød, width=0.4, align='edge', color='red')
    plt.show()

if __name__ == "__main__":
    kurvediagram()
    punktdiagram()
    stolpediagram()
    dobbel_stolpediagram()
