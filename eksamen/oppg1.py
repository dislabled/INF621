#!/usr/bin/env python3
# coding=utf-8

from json import loads

def lesjson(filnavn:str) -> dict:
    """
    Leser en JSON fil og returnerer en dict med mutasjonsnavn som nøkler
    Tilhørende registrerte smittetilfeller er en liste med ints

    args: 
        filnavn:str - filnavn på json fil som skal leses

    returns:
        smitte:dict - Ordbok som beskrevet over
    """
    with open(filnavn, 'r') as fil:
        smitte = {}
        tabell = loads(fil.read())
        for nøkkel in tabell:
            smitte[nøkkel] = tabell[nøkkel]
    return(smitte)


if __name__ == "__main__":
    print(lesjson('smitte.json'))
