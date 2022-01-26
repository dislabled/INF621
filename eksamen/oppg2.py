#!/usr/bin/env python3
# coding=utf-8

from oppg1 import lesjson

def utvikling(data:dict, mutasjoner:list) -> list:
    """
    Lager en liste over totalt antall smittetilfeller hver dag, per
    oppgitt mutasjon.

    args:
        data:dict - Ordbok med smittetilfeller
        mutasjoner:list - Liste over mutasjoner vi vil summere

    returns:
        totalt:list - liste over total smittetilfeller per dag
    """
    totalt = [0]*len(list(data.values())[0])
    for mut in mutasjoner:
        if mut in data:
            for i, dag in enumerate(data[mut]):
                totalt[i] += dag
    return totalt

if __name__ == "__main__":
    smitte = lesjson('smitte.json')
    print(utvikling(smitte, ['alfa', 'beta', 'delta']))
    print(utvikling(smitte, ['omikron']))
