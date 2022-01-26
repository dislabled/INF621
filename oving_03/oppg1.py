#!/usr/bin/env python3
# coding=utf-8

from random import randint
from csv import writer

# Oppgave 1.a
def tellkast(m, n):
    """
    kaster (m)antall terninger
    """
    kast_liste = []
    antall_kast = 0
    while n not in kast_liste:
        antall_kast += 1
        kast_liste = []
        for _ in range(m):
            kast_liste.append(randint(1, n))
    return antall_kast

# Oppgave 1.b
with open('kast.csv', 'w') as f:
    w = writer(f, delimiter=';')
    n_linje = [' ']
    for j in range(1,21):
        n_linje.append('n='+str(j))
    w.writerow(n_linje)
    for i in range(1,19):
        m_linje = []
        m_linje.append('m='+str(i))
        for j in range(1,21):
            m_linje.append(tellkast(j,i))
        w.writerow(m_linje)

