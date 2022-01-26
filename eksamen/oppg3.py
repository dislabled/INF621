#!/usr/bin/env python3
# coding=utf-8

import matplotlib.pyplot as plt
from oppg1 import lesjson
from oppg2 import utvikling
from datetime import datetime

def kurve(data:dict, mutasjoner:list) -> None:
    """
    Plotter en kurve over antall nye smittetilfeller som en funksjon av tid

    args:
        data:dict - Ordbok med smittetilfeller
        mutasjoner:list - Liste over mutasjoner vi vil plotte
    """
    x = range(1, 11)
    for mut in mutasjoner:
        if mut in data:
            # print(data[mut])
            plt.plot(x, list(data[mut]), label=mut)
    if len(mutasjoner) >= 2:
        plt.plot(x, utvikling(data, mutasjoner), label='totalt')

    plt.title('Smitteutvikling siste 10 dager t.o.m. ' + datetime.now().strftime('%d.%m.%y'))
    plt.ylabel('Antall smittetilfeller')
    plt.xlabel('Dag')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    smitte = lesjson('smitte.json')
    kurve(smitte, ['alfa', 'beta', 'delta'])
    kurve(smitte, ['omikron'])
