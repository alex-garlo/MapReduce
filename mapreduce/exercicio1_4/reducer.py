#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey+"\t"+str(salesTotal))
        oldKey = thisKey

    oldKey = thisKey
    if float(thisSale) > salesTotal:
        salesTotal = float(thisSale)

if oldKey != None:
    print(oldKey+"\t"+str(salesTotal))

