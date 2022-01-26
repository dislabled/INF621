#!/usr/bin/env python3
# coding=utf-8


# Oppgave 2.a
from datetime import datetime, date
from locale import setlocale, LC_TIME

setlocale(LC_TIME, 'nb_NO.utf-8')

def svar_paa_2a():
    svar1 = "Nøkkel kan bare forekomme 1 gang, flere passeringer kan være samme tid"
    svar2 = "Nøkkel kan bare forekomme 1 gang, skiltnummer kan forekomme flere ganger i ordboken"
    svar3 = "Den samme bilen kan ikke passere fotoboksen to ganger til samme tidspunkt"
    print('Tidspunkt bør ikke brukes som nøkkel alene fordi:\n {}'.format(svar1))
    print('Bilnummer bør ikke brukes som nøkkel alene fordi:\n {}'.format(svar2))
    print('Tuplen kan brukes som nøkkel fordi:\n {}'.format(svar3))

# Oppgave 2.b
def hent_fotoboksdata():
    """
    Parser filen fotoboks.txt og returnerer info som en ordbok
    """
    fotoboksdata = {}
    with open('fotoboks.txt', 'r') as fil:
        for lines in fil.readlines():
            # 14.11.2021-09:46:01 TA871455 75
            tidspunkt = datetime.strptime(lines[0:19], '%d.%m.%Y-%H:%M:%S')
            fotoboksdata[(tidspunkt, lines[21:28])] = lines[29:].strip()
    return fotoboksdata

# Oppgave 2.c
def antall_bøter(start_t, slutt_t, målinger):
    """
    Returnerer antall bøter(bøter) gitt fra (start_t) tiden til (slutt_t) tiden
    """
    bøter = 0
    for tid, skilt in målinger:
        if start_t <= tid and slutt_t > tid:
            if int(målinger[(tid, skilt)]) > 80:
                bøter += 1
    return bøter

# Oppgave 2.d
def fartsbøter(målinger):
    """
    Skriver en linje med antall bøter per dag, i filen [bøter_per_dag.txt] fra
    tidspunktet start_t til slutt_t
    """
    start_t = date(2021, 11, 8)
    slutt_t = date(2021, 11, 15)
    bøter_per_dag = {}
    for tid, skilt in målinger:
        if start_t <= tid.date() and slutt_t > tid.date():
            if int(målinger[(tid, skilt)]) > 80:
                dag = bøter_per_dag.get(tid.date(), 0)
                bøter_per_dag[tid.date()] = dag + 1
    with open('bøter_per_dag.txt', 'w') as fil:
        for nøkkel in sorted(bøter_per_dag):
            fil.write('{}: {} bøter\n'.format(datetime.strftime(nøkkel, '%A %d. %B').title(), bøter_per_dag[nøkkel]))

if __name__ == "__main__":
    svar_paa_2a()
    målinger = hent_fotoboksdata()
    start_t = datetime(2021, 11, 8, 0, 0, 0)
    slutt_t = datetime(2021, 11, 15, 0, 0, 0)
    print(antall_bøter(start_t, slutt_t, målinger))
    fartsbøter(målinger)
