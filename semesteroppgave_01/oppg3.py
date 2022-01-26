#!/usr/bin/env python3
# coding=utf-8

from oppg1 import antall

# Oppgave 3.a
def lag_krypteringsordbok():
    """
    Returnerer en ordbok med nøkkel[bokstav] som skal byttes med verdi[bokstav]
    """
    ordbok = {}
    with open('hemmelig.txt', 'r') as fil:
        for linjer in fil.readlines():
            ordbok[linjer[0]] = linjer[16]
    return ordbok

# Oppgave 3.b
def krypter(filnavn, krypteringsordbok):
    """
    Åpner (filnavn) for kryptering via (krypteringsordbok) og skriver til
    kryptert_(filnavn)
    """
    with open(filnavn, 'r') as ukrypt_fil:
        with open('kryptert_'+filnavn, 'w') as krypt_fil:
            for bokstav in ukrypt_fil.read():
                if bokstav in krypteringsordbok:
                    krypt_fil.write(krypteringsordbok[bokstav])
                else:
                    krypt_fil.write(bokstav)

# Oppgave 3.c
def dekrypter(filnavn, krypteringsordbok):
    """
    Åpner (filnavn) for dekryptering via (krypteringsordbok) og skriver til
    dekryptert_(filnavn)
    """
    dekrypteringsordbok = {}
    for nøkkel in krypteringsordbok:
        dekrypteringsordbok[krypteringsordbok[nøkkel]] = nøkkel
    with open(filnavn, 'r') as krypt_fil:
        with open('dekryptert_'+filnavn, 'w') as dekrypt_fil:
            for bokstav in krypt_fil.read():
                if bokstav in dekrypteringsordbok:
                    dekrypt_fil.write(dekrypteringsordbok[bokstav])
                else:
                    dekrypt_fil.write(bokstav)

# Oppgave 4.a
def frekvens_av_bokstaver(filnavn):
    """
    Finner frekvensen av ulike bokstaver i (filnavn) og returnerer en
    sortert liste
    """
    ordbok_frek = antall(filnavn)
    return sorted(ordbok_frek, key=ordbok_frek.get, reverse=True)

def lag_dekryptordbok(frekvens, alfabet):
    """
    Lager dekrypteringsordbok av frekvens samt et alfabet
    """
    sannsynlig_ordbok = {}
    indeks = 0
    for tegn in alfabet:
        sannsynlig_ordbok[tegn] = frekvens[indeks]
        indeks += 1
    return sannsynlig_ordbok


if __name__ == "__main__":
    krypteringsordbok = lag_krypteringsordbok()
    krypter('test.txt', krypteringsordbok)
    dekrypter('kryptert_test.txt', krypteringsordbok)
    # Oppgave 4.b
    sannsynlig_alfabet = "etaoinshrdlcumwfgypbvkjxqzæøå"
    # Oppgave 4.c
    sannsynlig_alfabet = "etaonihsrdlumwcfgypbvkxqjzæøå"
    frekvens = frekvens_av_bokstaver('en_kryptert_melding.txt')
    test_ordbok = lag_dekryptordbok(frekvens, sannsynlig_alfabet)
    dekrypter('en_kryptert_melding.txt', test_ordbok)
