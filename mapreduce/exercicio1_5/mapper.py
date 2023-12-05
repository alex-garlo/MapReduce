#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 6:
        continue
    
    date, time, store, item, cost, payment = data
    clave = "El coste total de ventas es:"
    print(clave+"\t"+cost)
