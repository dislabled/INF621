#!/usr/bin/env python3
# coding=utf-8

from json import loads
from requests import get
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 4})
# Oppgave 2.a
# Oppgave 2.b
url = 'https://data.ssb.no/api/v0/dataset/26975.json?lang=no'
data = loads(get(url).text)['dataset']
# with open('dataset.json', 'r') as file:
#     data = loads(file.read())['dataset']

index = data['dimension']['Region']['category']['index']
label = data['dimension']['Region']['category']['label']
years = data['dimension']['Tid']['category']['index']
value = data['value']

table = {}
years = sorted(years)
beg_year = int(years[0])
end_year = int(years[-1])
length = len(years)
for id in label:
    start = value[index[id]*length]
    end = value[index[id]*length+(length-1)]
    if min(value[length*index[id]:length*(index[id]+1)]) >0:
        diff = end - start
        table[id] = (diff, start, end)

# Oppgave 2.c
top8 = sorted(table, key=table.get)[:8]
areas = []
first_year = []
last_year = []
for id in top8:
    areas.append(label[id])
    first_year.append(table[id][1])
    last_year.append(table[id][2])
plt.bar(areas, first_year, width=-0.4, align='edge', color='green', label=min(years))
plt.bar(areas, last_year, width=0.4, align='edge', color='red', label=max(years))
plt.legend()
plt.show()

# Oppgave 2.d
top = []
for year in range(beg_year, end_year+1):
    top.append(value[length*index[top8[0]]+year-beg_year])
plt.grid(color='black', linestyle='-', linewidth=0.2)
print(years)
plt.plot(years, top)
plt.title('Residential decline in ' + label[top8[0]])
plt.ylabel('Residents')
plt.xlabel('Year')
# plt.show()
