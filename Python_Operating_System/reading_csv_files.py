#!/usr/bin/env python3

import csv

f = open("CSV.txt")
csv_f = csv.reader(f)
for row in csv_f:
    Name,Phone,Role = row
    print("Name:{},Phone:{},Role:{}".format(Name,Phone,Role))
