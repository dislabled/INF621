#!/usr/bin/env python3
# coding=utf-8

from datetime import timedelta, datetime

# Oppgave 3.a
def tidspunkt_om(n):
    """ Skriver ut tidspunktet som inntreffer etter (n) sekunder """
    nå = datetime.now()
    om = timedelta(seconds=n)
    print(nå + om)

# Oppgave 3.b
def dato_til(dato):
    """
    Returnerer timedelta objekt/differansen til (dato) 
    """
    nå = datetime.now()
    if dato < nå:
        dato = datetime(nå.year+1, dato.month, dato.day)
    return dato - nå

def skriv_ut(streng, dag):
    """ Formaterer og skriver ut basert på (streng) og (dag) """
    print("Antall hele dager igjen til {}: {}".format(streng, dag))

def nedtelling():
    """
    Setter opp datoer som lagt opp i oppgave 3.b
    """
    nå = datetime.now()
    dato_nyttårsdag = datetime(nå.year, 1, 1)
    dato_neste_måned = datetime(nå.year, nå.month+1, 1, 1)
    dato_eksamen = datetime(nå.year, 12, 17)
    dato_julaften = datetime(nå.year, 12, 24)
    dato_inovember = datetime(nå.year, 11, 4, 15, 59, 54)
    skriv_ut("nyttårsdag", dato_til(dato_nyttårsdag).days)
    skriv_ut("neste måned", dato_til(dato_neste_måned).days)
    skriv_ut("eksamen", dato_til(dato_eksamen).days)
    skriv_ut("julaften", dato_til(dato_julaften).days)
    skriv_ut("4. november klokken 15:59:54", dato_til(dato_inovember).days)


if __name__ == "__main__":
    tidspunkt_om(1)
    tidspunkt_om(60)
    tidspunkt_om(31536000)
    nedtelling()
