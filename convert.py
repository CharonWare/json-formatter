#!/usr/bin/python3

from sys import argv

inFile = argv[1]

tds = {}

with open(inFile) as file:

    for line in file:
        f = line.split(" : ")
        tds.update({f[0].strip() : f[1].strip()})

for key,value in tds.items():
    print(f'                {{\n                    "name": "{key}",\n                    "value": "{value}"\n                }},')
