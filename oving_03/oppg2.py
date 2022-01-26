#!/usr/bin/env python3
# coding=utf-8

from csv import reader, writer
from datetime import datetime


# Oppgave 2.a
def les_csv(filnavn):
    with open(filnavn, 'r') as f:
        r = reader(f)
        liste = []
        for linje in r:
            liste.append(linje)
    return liste

def separer_data():
    data = les_csv('florida.csv')
    tabell = {0 :['min_vind', 'maks_vind', 'tot_nedbør', 'min_temp', 'maks_temp']}
    for måned in range(1,11):
        min_vind = 100
        max_vind = 0
        tot_nedbør = 0
        min_temp = 100
        max_temp = 0
        for i in range(1,len(data)):
            dag = datetime.strptime(data[i][0], '%d.%m.%Y').date()
            if dag.month == måned:
                if float(data[i][1]) < min_vind:
                    min_vind = float(data[i][1])
                if float(data[i][1]) > max_vind:
                    max_vind = float(data[i][1])
                if float(data[i][3]) < min_temp:
                    min_temp = float(data[i][3])
                if float(data[i][4]) < max_temp:
                    max_temp = float(data[i][4])
                tot_nedbør += float(data[i][2])
        tabell[str(måned)] = [min_vind, max_vind, tot_nedbør, min_temp, max_temp]
    return tabell

def write_csv(filnavn):
    with open(filnavn, 'w') as f:
        w = writer(f, delimiter=',')
        for liste in separer_data().values():
            w.writerow(liste)

if __name__ == "__main__":
    write_csv('måned.csv')
